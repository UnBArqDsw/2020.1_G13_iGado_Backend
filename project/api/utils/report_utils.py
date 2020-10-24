class ReportUtils:

    def calculate_gmd(farm):
        return {
            'abc': 'xyz'
        }
        # beef_cattles = [beef_cattle for beef_cattle in farm.beef_cattles]
        # individual_gmd = []
        # total_gmd = 0
        # for beef_cattle in beef_cattles:
        #     gmd = (beef_cattle.actual_weight - beef_cattle.last_weight)/(beef_cattle.actual_day_of_weighing - beef_cattle.last_day_of_weighing) 
        #     individual_gmd.append(gmd)
        #     total_gmd+=gmd
        # total_gmd = total_gmd/len(individual_gmd)
        # return {
        #     'beef_cattle_id': [beef_cattle.id for beef_cattle in beef_cattles],
        #     'beef_cattle_name': [beef_cattle.name for beef_cattle in beef_cattles],
        #     'beef_cattle_gmd': individual_gmd,
        #     'total_gmd': total_gmd
        # }

    def calculate_heads_rate(farm):
        return {
            'def' : 'uvw'
        }
        # total_cattles = 0
        # total_cattles += len(farm.beef_cattle)
        # total_cattles += len(farm.dairy_cattle)
        
        # heads_rate = total_cattles / farm.size_farm

        # return {
        #     'heads_rate': heads_rate
        # }