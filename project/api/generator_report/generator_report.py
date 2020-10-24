from project.api.models.report import GeneralReportModel
from project.api.models.report import ReportGMDModel


class ReportGenerator:

    def generate(self, user_id, type, farm_id):
        generator = _get_report_type(type)
        return generator(farm_id, user_id)

    
def _get_report_type(type):
    if type == 'GMD':
        return _generate_gmd_report
    elif type == 'general':
        return _generate_general_report
    else:
        raise ValueError(type)

def _generate_gmd_report(farm_id, user_id):
    report = ReportGMDModel(farm_id)
    return_report_gmd = report.CONST_TEMPLATE_METHOD(user_id)
    return return_report_gmd

def _generate_general_report(farm_id, user_id):
    report = GeneralReportModel(farm_id)
    return_report_general = report.CONST_TEMPLATE_METHOD(user_id)
    return return_report_general