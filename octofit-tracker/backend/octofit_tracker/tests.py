from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='Test Team')
        self.assertEqual(str(t), 'Test Team')
    def test_user_create(self):
        t = Team.objects.create(name='Test Team2')
        u = User.objects.create(name='Test User', email='test@example.com', team=t.name)
        self.assertEqual(str(u), 'Test User')
    def test_activity_create(self):
        a = Activity.objects.create(user_email='test@example.com', type='Run', duration=10, date='2024-01-01')
        self.assertEqual(a.type, 'Run')
    def test_workout_create(self):
        w = Workout.objects.create(name='W1', description='desc', suggested_for=['Test Team'])
        self.assertEqual(w.name, 'W1')
    def test_leaderboard_create(self):
        l = Leaderboard.objects.create(team='Test Team', points=10)
        self.assertEqual(l.points, 10)
