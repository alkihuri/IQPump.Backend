# Duel model
import datetime


class Duel(db.Model):   
    def __init__(self, challenger_id, opponent_id):
        self.challenger_id = challenger_id
        self.opponent_id = opponent_id
        self.created_at = datetime.datetime.now()
        self.status = 'pending'
        self.winner_id = None
        self.loser_id = None
        self.updated_at = None
        self.deleted_at = None