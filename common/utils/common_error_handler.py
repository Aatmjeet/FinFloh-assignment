
def common_error_handler(error):
	status_code = 500  # Internal Server Error
	if hasattr(error, 'code'):
		code = error.code
	if isinstance(error, ValueError):
		status_code = 400  # Bad Request

	response = {
		'error': str(error),
	}
	return {'error': str(error)}, status_code
