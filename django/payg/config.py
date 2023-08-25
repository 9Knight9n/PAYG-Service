UNIFORM_COST = 0.001
API_COST = {
    "/api/payg/api1/": UNIFORM_COST,
    "/api/payg/api2/": UNIFORM_COST,
    "/api/payg/api3/": UNIFORM_COST,
    "/api/payg/api4/": UNIFORM_COST,
}
LOGGER_ALLOWED_NAMESPACES = ['payg']
LOGGER_ALLOWED_STATUS_CODES = [200, 201, 202, 203, 204]
