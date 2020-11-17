from project.api.models.reproduction_management import ReproductionManagementModel
from project.api.models.weighing_management import WeighingManagementModel
from project.api.models.beef_cattle import BeefCattle
from project import db


class ManagementGenerator:

    def generate(self, type, management_data):
        generator = _get_report_type(type)
        management = generator(management_data)
        db.session.add(management)
        db.session.commit()
        return management

    
def _get_report_type(type):
    if type == 'weighing_management':
        return _generate_weighing_management
    elif type == 'reproduction_management':
        return _generate_reproduction_management
    else:
        raise ValueError(type)

def _generate_weighing_management(management_data):
    beef_cattle = BeefCattle.query.filter_by(bovine_id=int(management_data['bovine_id'])).first()
    weighing_management = WeighingManagementModel(
                         date_of_old_weighing=beef_cattle.date_of_actual_weighing,
                         actual_weight=management_data['actual_weight'],
                         bovine_id=management_data['bovine_id'],
                         old_weight=beef_cattle.actual_weight)
    beef_cattle.actual_weight = management_data['actual_weight']
    db.session.add(beef_cattle)
    db.session.commit()
    return weighing_management

def _generate_reproduction_management(management_data):
    reproduction_management = ReproductionManagementModel(
            bovine_id=management_data['bovine_id'],
            bull_breed=management_data['bull_breed'],
            reproduction_type=management_data['reproduction_type'])
    if 'bull_id' in management_data.keys():
        reproduction_management.bull_id = management_data['bull_id']
    if management_data['reproduction_type'] == "insemination":
        reproduction_management.insemination_period = []
        reproduction_management.insemination_amount = management_data['insemination_amount']
        reproduction_management.insemination_period += management_data['insemination_period']
    return reproduction_management
