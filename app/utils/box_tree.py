from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any

class JobType(Enum):
    """Enum for Autosys job types."""
    BOX = "BOX"
    COMMAND = "CMD"
    FILE_WATCHER = "FW"
    UNKNOWN = "UNKNOWN"

@dataclass
class AutosysJobNode:
    """Node in the Autosys job tree."""
    name: str
    job_type: JobType
    attributes: Dict[str, Any] = field(default_factory=dict)
    children: List['AutosysJobNode'] = field(default_factory=list)
    parent: Optional['AutosysJobNode'] = None
    
    def add_child(self, child: 'AutosysJobNode') -> None:
        """Add a child node to this node."""
        child.parent = self
        self.children.append(child)
    
    def find_job_by_name(self, job_name: str) -> Optional['AutosysJobNode']:
        """Find a job by name in the tree."""
        if self.name == job_name:
            return self
        
        for child in self.children:
            result = child.find_job_by_name(job_name)
            if result:
                return result
        
        return None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the node to a dictionary."""
        result = {
            "name": self.name,
            "job_type": self.job_type.value,
            "attributes": self.attributes,
            "children": [child.to_dict() for child in self.children]
        }
        return result

class AutosysBoxTree:
    """Tree representation of Autosys box structure."""
    
    def __init__(self):
        """Initialize an empty tree."""
        self.root = None
        self.jobs_by_name: Dict[str, AutosysJobNode] = {}
    
    def load_from_jil(self, jil_content: str) -> None:
        """Load a tree from JIL content."""
        lines = jil_content.splitlines()
        current_job = None
        jobs = {}
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith("/*"):
                continue
                
            if line.startswith("insert_job:"):
                parts = line.split()
                job_name = parts[1]
                job_type = JobType(parts[3])
                
                current_job = AutosysJobNode(
                    name=job_name,
                    job_type=job_type,
                    attributes={}
                )
                jobs[job_name] = current_job
                
                if job_type == JobType.BOX and not self.root:
                    self.root = current_job
            elif line.startswith("box_name:"):
                box_name = line.split()[1]
                if box_name in jobs:
                    jobs[box_name].add_child(current_job)
            elif ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip().strip('"')
                current_job.attributes[key] = value
        
        self.jobs_by_name = jobs
    
    def get_job_by_name(self, job_name: str) -> Optional[AutosysJobNode]:
        """Get a job by name."""
        return self.jobs_by_name.get(job_name)
    
    def get_jobs_by_box(self, box_name: str) -> List[AutosysJobNode]:
        """Get all jobs in a box."""
        box = self.get_job_by_name(box_name)
        if not box or box.job_type != JobType.BOX:
            return []
        
        return box.children
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the tree to a dictionary."""
        if not self.root:
            return {}
        
        return self.root.to_dict()