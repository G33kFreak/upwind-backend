from users.models.user import User
from relapses.models import Relapse

from difflib import get_close_matches


class RelapseReportCreator:

    def __init__(self, validated_data: dict = None, user: User = None):
        self.user = user
        self.validated_data = validated_data

    def __call__(self, *args, **kwds):
        return self.create_report()

    def create_report(self):
        relapses = Relapse.objects.all()
        reasons = []
        matches = []

        for relapse in relapses:
            reasons.append(relapse.reason)

        for reason in reasons:
            matches.append(get_close_matches(reason, reasons, cutoff=0.65))

        best_match = max(enumerate(matches), key=(lambda x: len(x[1])))[1]
        best_match_objects = [
            relapse for relapse in relapses if relapse.reason in best_match
        ]
        

        
        return {"message": str(best_match_objects)}
