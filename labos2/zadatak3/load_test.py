import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):

	@task
	def load_test(self):
		self.client.get(url="/0/3.14159")