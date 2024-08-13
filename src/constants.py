# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.

from pathlib import PurePath
from string import Template

# Charm constants
POSTGRESQL_DSN_TEMPLATE = Template("postgres://$username:$password@$endpoint/$database")
WORKLOAD_CONTAINER = "hydra"
WORKLOAD_SERVICE = "hydra"
COOKIE_SECRET_KEY = "cookie"
SYSTEM_SECRET_KEY = "system"
COOKIE_SECRET_LABEL = "cookie-secret"
SYSTEM_SECRET_LABEL = "system-secret"
DEFAULT_OAUTH_SCOPES = ["openid", "profile", "email", "phone"]
DEFAULT_RESPONSE_TYPES = ["code"]

# Application constants
HYDRA_SERVICE_COMMAND = "hydra serve all"
PUBLIC_PORT = 4444
ADMIN_PORT = 4445
CONFIG_FILE_NAME = "/etc/config/hydra.yaml"
LOG_DIR = PurePath("/var/log")
LOG_FILE = LOG_DIR / "hydra.log"

# Integration constants
DATABASE_INTEGRATION_NAME = "pg-database"
PUBLIC_INGRESS_INTEGRATION_NAME = "public-ingress"
ADMIN_INGRESS_INTEGRATION_NAME = "admin-ingress"
INTERNAL_INGRESS_INTEGRATION_NAME = "internal-ingress"
LOGIN_UI_INTEGRATION_NAME = "ui-endpoint-info"
PEER_INTEGRATION_NAME = "hydra"
PROMETHEUS_SCRAPE_INTEGRATION_NAME = "metrics-endpoint"
LOKI_API_PUSH_INTEGRATION_NAME = "logging"
GRAFANA_DASHBOARD_INTEGRATION_NAME = "grafana-dashboard"
TEMPO_TRACING_INTEGRATION_NAME = "tracing"
OAUTH_INTEGRATION_NAME = "oauth"
