from test_db.settings import PORTAL_URL


def students_proc(request):
	return {'PORTAL_URL': PORTAL_URL}


