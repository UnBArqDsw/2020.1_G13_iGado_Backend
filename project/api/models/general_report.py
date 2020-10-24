from project.api.models.report import ReportAbstract
from project.api.utils.report_utils import ReportUtils
from project.api.models.farm import FarmModel



class GeneralReportModel(ReportAbstract):
    __tablename__ = 'report'

    __mapper_args__ = {
        'polymorphic_identity': 'report'
    }

    def __init__(self, farm_id):
        self.farm_id = farm_id

    def generate_metric(self):
        farm = FarmModel.query.filter_by(farm_id=int(self.farm_id)).first()
        gmd = ReportUtils.calculate_gmd(farm)
        heads_rate = ReportUtils.calculate_heads_rate(farm)
        # iabcz = calculate_iabcz(farm)
        return {
            'metrics': [gmd, heads_rate]
        }

    def generate_graphic(self):
        pass