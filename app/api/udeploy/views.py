import requests
from typing import Dict, Any
from flask import current_app
from .schemas import ResponseSchema

class UdeployService:
    """Service layer for uDeploy operations"""

    @staticmethod
    def _make_request(url: str, method: str='GET', params=None, data=None) -> Dict:
        try:
            response = requests.request(
                method=method,
                url=url,
                auth=(current_app.config['UDEPLOY_USER'], current_app.config['UDEPLOY_PASSWORD']),
                params=params,
                json=data,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            current_app.logger.error(f"uDeploy API error: {str(e)}")
            return None

    @staticmethod
    def run_process(data: Dict) -> Dict[str, Any]:
        """Trigger uDeploy process"""
        try:
            api_url = f"{current_app.config['UDEPLOY_BASE_URL']}/process"
            result = UdeployService._make_request(api_url, 'POST', data=data)
            if not result:
                return {'data': None, 'message': '触发流程失败', 'code': -1}
            return {'data': result, 'message': '流程触发成功', 'code': 0}
        except Exception as e:
            return {'data': None, 'message': f"触发流程异常: {str(e)}", 'code': -1}

    @staticmethod
    def get_workflow_trace(request_id: str) -> Dict[str, Any]:
        """Get workflow trace by request ID"""
        try:
            api_url = f"{current_app.config['UDEPLOY_BASE_URL']}/trace/{request_id}"
            result = UdeployService._make_request(api_url)
            if not result:
                return {'data': None, 'message': '获取工作流跟踪失败', 'code': -1}
            return {'data': result, 'message': '获取跟踪成功', 'code': 0}
        except Exception as e:
            return {'data': None, 'message': f"获取跟踪异常: {str(e)}", 'code': -1}

    @staticmethod
    def get_deployment_logs(log_path: str) -> Dict[str, Any]:
        """Get deployment logs from uDeploy"""
        try:
            api_url = f"{current_app.config['UDEPLOY_BASE_URL']}/logs"
            result = UdeployService._make_request(api_url, params={'path': log_path})
            if not result:
                return {'data': None, 'message': '获取日志失败', 'code': -1}
            return {'data': result, 'message': '获取日志成功', 'code': 0}
        except Exception as e:
            return {'data': None, 'message': f"获取日志异常: {str(e)}", 'code': -1}