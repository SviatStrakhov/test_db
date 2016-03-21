from django.core.management.base import BaseCommand

from testdb.models import Student, Group


class Command(BaseCommand):
	args = '<model_name model_name ...>'
	help = "Prints to console number of student related objects in adatabase."


	def handle(self, *args, **options):
		if 'students' in args:
			for student in Student.objects.all():
				print(student)
		if 'groups' in args:
			for group in Group.objects.all():
				print(group)