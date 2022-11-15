import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):

	@task
	def load_test(self):
		self.client.get(url="/0/3.14159")

# https://www.youtube.com/watch?v=SOu6hgklQRA&ab_channel=NicolaiGram
# locust -f .\load_test.py --host htpp://localhost:5000