from typing import List, Optional, Dict, Any
from app.api.autosys.models import AutosysJob, AutosysJobModel
from app.api.autosys.schemas import AutosysJobSchema, ResponseSchema
from app.api.udeploy.views import UdeployService

class AutosysService:
    """Service layer for Autosys operations."""
    
    @staticmethod
    def get_all_jobs() -> Dict[str, Any]:
        """Get all Autosys jobs."""
        try:
            jobs = AutosysJobModel.get_all_jobs()
            # 调用udeploy服务获取相关信息
            udeploy_data = UdeployService.get_workflow_trace(jobs[0].job_name if jobs else "")
            
            schema = AutosysJobSchema(many=True)
            return ResponseSchema().dump({
                'data': {
                    'autosys_jobs': schema.dump(jobs),
                    'udeploy_info': udeploy_data
                },
                'message': "获取所有作业成功",
                'code': 0
            })
        except Exception as e:
            return ResponseSchema().dump({
                'data': None,
                'message': f"获取作业失败: {str(e)}",
                'code': -1  
            })

    @staticmethod
    def get_job_by_name(job_name: str) -> Dict[str, Any]:
        """Get a specific Autosys job by name."""
        try:
            job = AutosysJobModel.get_job_by_name(job_name)
            if not job:
                return ResponseSchema().dump({
                    'data': None,
                    'message': f"未找到作业: '{job_name}'",
                    'code': -1
                })
            
            schema = AutosysJobSchema()
            return ResponseSchema().dump({
                'data': schema.dump(job),
                'message': f"获取作业 '{job_name}' 成功",
                'code': 0
            })
        except Exception as e:
            return ResponseSchema().dump({
                'data': None,
                'message': f"获取作业失败: {str(e)}",
                'code': -1
            })