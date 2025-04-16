from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Optional, List, Any

@dataclass
class AutosysJob:
    """Data model for Autosys Job."""
    job_name: str
    job_type: str
    owner: Optional[str] = None
    machine: Optional[str] = None
    condition: Optional[str] = None
    box_name: Optional[str] = None
    attributes: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Initialize the attributes dictionary if it's None."""
        if self.attributes is None:
            self.attributes = {}
    
    def get_attribute(self, key: str, default: Any = None) -> Any:
        """Get an attribute value by key."""
        return self.attributes.get(key, default)
    
    def set_attribute(self, key: str, value: Any) -> None:
        """Set an attribute value by key."""
        self.attributes[key] = value

class AutosysJobModel:
    """Data access layer for Autosys Jobs."""
    
    @staticmethod
    def get_all_jobs():
        """
        Mock implementation to get all jobs.
        In a real implementation, this would interact with the Autosys system.
        """
        # This is a mock implementation
        job1 = AutosysJob(
            job_name="box_level_top",
            job_type="BOX",
            owner="user@linux.host.net",
            machine="linux.host.net"
        )
        job1.set_attribute("description", "This is the top-level box job that encapsulates all other jobs and sub-boxes.")
        job1.set_attribute("date_conditions", 1)
        job1.set_attribute("days_of_week", "all")
        job1.set_attribute("start_times", "00:00")
        job1.set_attribute("alarm_if_fail", 0)
        job1.set_attribute("alarm_if_terminated", 0)
        
        job2 = AutosysJob(
            job_name="watch_input_file",
            job_type="FW",
            owner="user@linux.host.net"
        )
        job2.set_attribute("description", "File watcher job to monitor input file arrival")
        job2.set_attribute("box_name", "box_level_top")
        job2.set_attribute("watch_file", "/data/input/incoming.txt")
        job2.set_attribute("watch_interval", 60)
        job2.set_attribute("alarm_if_fail", 1)
        job2.set_attribute("alarm_if_terminated", 1)
        
        return [job1, job2]

    @staticmethod
    def get_job_by_name(job_name: str) -> Optional[AutosysJob]:
        """
        Mock implementation to get a job by name.
        In a real implementation, this would interact with the Autosys system.
        """
        jobs = AutosysJobModel.get_all_jobs()
        return next((job for job in jobs if job.job_name == job_name), None)
    
    @staticmethod
    def get_jobs_by_type(job_type: str) -> List[AutosysJob]:
        """
        Mock implementation to get all jobs of a specific type.
        In a real implementation, this would interact with the Autosys system.
        """
        jobs = AutosysJobModel.get_all_jobs()
        return [job for job in jobs if job.job_type == job_type]
    
    @staticmethod
    def get_jobs_by_parent(parent_name: str) -> List[AutosysJob]:
        """
        Mock implementation to get all jobs that belong to a specific parent job.
        In a real implementation, this would interact with the Autosys system.
        """
        jobs = AutosysJobModel.get_all_jobs()
        return [job for job in jobs if job.get_attribute("box_name") == parent_name]