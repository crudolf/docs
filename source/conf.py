# Mattermost documentation configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import os


def setup(app):
    return


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../extensions'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '3.4.3'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosectionlabel',
    'myst_parser',
    # `reredirects` is a local clone of sphinx_reredirects with parallel
    # read and write support enabled.
    # The original sphinx_reredirects extension can be found at:
    # https://documatt.gitlab.io/sphinx-reredirects/
    'reredirects',
    # `sitemap` is a local clone of sphinx_sitemap with parallel read
    # and write support enabled.
    # The original sphinx_sitemap extension can be found at:
    # https://pypi.org/project/sphinx-sitemap/
    'sitemap'
]

# Prefix document path to section labels, otherwise autogenerated labels would look like 'heading'
# rather than 'path/to/file:heading'
autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# Redirects using: https://pypi.org/project/sphinx-reredirects/
redirects = {

    "integrations/jira": "https://mattermost.gitbook.io/plugin-jira/",
    "integrations/zoom": "https://mattermost.gitbook.io/plugin-zoom/",
    "integrations/net-promoter-score": "https://docs.mattermost.com/manage/user-satisfaction-surveys.html",
    "developer/localization": "https://handbook.mattermost.com/contributors/contributors/localization",
    "overview/product": "https://docs.mattermost.com/about/product.html",
    "overview/security": "https://docs.mattermost.com/about/security.html",
    "overview/integrations": "https://docs.mattermost.com/about/integrations.html",
    "overview/license-and-subscription": "https://docs.mattermost.com/about/licensing-and-subscription.html",
    "overview/auth": "https://docs.mattermost.com/about/corporate-directory-integration.html",
    "overview/compliance": "https://docs.mattermost.com/about/certifications-and-compliance.html",
    "overview/faq": "https://docs.mattermost.com/about/frequently-asked-questions.html",
    "overview/architecture": "https://docs.mattermost.com/getting-started/architecture-overview.html",
    "getting-started/implementation_plan": "https://docs.mattermost.com/getting-started/implementation-plan.html",
    "getting-started/welcome_email": "https://docs.mattermost.com/getting-started/welcome-email-to-end-users.html",
    "guides/orchestration": "https://docs.mattermost.com/about/orchestration.html",
    "guides/administrator": "https://docs.mattermost.com/guides/install-deploy-upgrade-scale.html",
    "install/requirements": "https://docs.mattermost.com/install/software-hardware-requirements.html",
    "install/install-ubuntu-2004": "https://docs.mattermost.com/install/installing-ubuntu-2004-LTS.html",
    "install/install-ubuntu-1804": "https://docs.mattermost.com/install/installing-ubuntu-1804-LTS.html",
    "install/mattermost-omnibus": "https://docs.mattermost.com/install/installing-mattermost-omnibus.html",
    "install/sockets-db": "https://docs.mattermost.com/install/setting-up-socket-based-mattermost-database.html",
    "install/ee-install": "https://docs.mattermost.com/install/enterprise-install-upgrade.html",
    "install/transport-encryption/config": "https://docs.mattermost.com/install/transport-encryption.html",
    "install/transport-encryption/config-mattermost":
        "https://docs.mattermost.com/install/proxy-to-mattermost-transport-encryption.html",
    "install/transport-encryption/config-database":
        "https://docs.mattermost.com/install/database-transport-encryption.html",
    "install/transport-encryption/config-cluster":
        "https://docs.mattermost.com/install/cluster-transport-encryption.html",
    "install/deploy-bitnami": "https://docs.mattermost.com/install/deploying-team-edition-on-bitnami.html",
    "install/docker-local-machine": "https://docs.mattermost.com/install/setting-up-local-machine-using-docker.html",
    "install/docker-ebs": "https://docs.mattermost.com/install/setting-up-aws-elastic-beanstalk-docker.html",
    "install/install-mmte-helm-gitlab-helm":
        "https://docs.mattermost.com/install/installing-team-edition-helm-chart.html",
    "install/desktop": "https://docs.mattermost.com/install/desktop-app-install.html",
    "install/desktop-managed-resources": "https://docs.mattermost.com/install/desktop-app-managed-resources.html",
    "install/desktop-msi-gpo":
        "https://docs.mattermost.com/install/desktop-msi-installer-and-group-policy-install.html",
    "install/smtp-email-setup": "https://docs.mattermost.com/configure/smtp-email.html",
    "install/config-cloudfront":
        "https://docs.mattermost.com/configure/configuring-cloudfront-to-host-mattermost-static-assets.html",
    "install/outbound-proxy": "https://docs.mattermost.com/configure/using-outbound-proxy.html",
    "install/i18n": "https://docs.mattermost.com/configure/enabling-chinese-japanese-korean-search.html",
    "install/config-apache2": "https://docs.mattermost.com/configure/configuring-apache2.html",
    "administration/telemetry": "https://docs.mattermost.com/manage/telemetry.html",
    "administration/changelog": "https://docs.mattermost.com/install/self-managed-changelog.html",
    "administration/image-proxy": "https://docs.mattermost.com/deploy/image-proxy.html",
    "administration/encryption": "https://docs.mattermost.com/deploy/encryption-options.html",
    "administration/backup": "https://docs.mattermost.com/deploy/backup-disaster-recovery.html",
    "administration/upgrade": "https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html",
    "administration/important-upgrade-notes": "https://docs.mattermost.com/upgrade/important-upgrade-notes.html",
    "administration/version-archive": "https://docs.mattermost.com/upgrade/version-archive.html",
    "administration/extended-support-release": "https://docs.mattermost.com/upgrade/extended-support-release.html",
    "administration/release-lifecycle": "https://docs.mattermost.com/upgrade/release-lifecycle.html",
    "administration/downgrade": "https://docs.mattermost.com/upgrade/downgrading-mattermost-server.html",
    "administration/open-source-components": "https://docs.mattermost.com/upgrade/open-source-components.html",
    "administration/release-definitions": "https://docs.mattermost.com/upgrade/release-definitions.html",
    "administration/performance-alerting-guide": "https://docs.mattermost.com/scale/peformance-alerting.html",
    "administration/config-settings": "https://docs.mattermost.com/configure/configuration-settings.html",
    "administration/config-in-database":
        "https://docs.mattermost.com/configure/configuation-in-mattermost-database.html",
    "administration/branding": "https://docs.mattermost.com/configure/custom-branding-tools.html",
    "deployment/deployment": "https://docs.mattermost.com/deploy/deployment-overview.html",
    "deployment/bots": "https://developers.mattermost.com/integrate/admin-guide/admin-bot-accounts/",
    "deployment/on-boarding": "https://docs.mattermost.com/getting-started/admin-onboarding-tasks.html",
    "deployment/ha": "https://docs.mattermost.com/deployment/cluster.html",
    "deployment/webrtc": "https://docs.mattermost.com/deployment/video-and-audio-calling.html",
    "deployment/bleve": "https://docs.mattermost.com/deploy/bleve-search.html",
    "deployment/desktop-app-deployment": "https://docs.mattermost.com/deploy/desktop-app.html",
    "deployment/scaling": "https://docs.mattermost.com/scale/scaling-for-enterprise.html",
    "deployment/cluster": "https://docs.mattermost.com/scale/high-availability-cluster.html",
    "deployment/elasticsearch": "https://docs.mattermost.com/scale/elasticsearch.html",
    "deployment/metrics": "https://docs.mattermost.com/scale/performance-monitoring.html",
    "deployment/customize-mattermost": "https://docs.mattermost.com/configure/customizing-mattermost.html",
    "deployment/customize-email": "https://docs.mattermost.com/configure/email-templates.html",
    "deployment/advanced-permissions": "https://docs.mattermost.com/onboard/advanced-permissions.html",
    "deployment/permissions-backend":
        "https://docs.mattermost.com/onboard/advanced-permissions-backend-infrastructure.html",
    "deployment/admin-roles": "https://docs.mattermost.com/onboard/system-admin-roles.html",
    "deployment/guest-accounts": "https://docs.mattermost.com/onboard/guest-accounts.html",
    "deployment/sso-ldap": "https://docs.mattermost.com/onboard/ad-ldap.html",
    "deployment/auth": "https://docs.mattermost.com/onboard/multi-factor-authentication.html",
    "deployment/sso-openidconnect": "https://docs.mattermost.com/onboard/sso-openidconnect.html",
    "deployment/sso-gitlab": "https://docs.mattermost.com/onboard/sso-gitlab.html",
    "deployment/sso-google": "https://docs.mattermost.com/onboard/sso-google.html",
    "deployment/sso-office": "https://docs.mattermost.com/onboard/sso-office.html",
    "deployment/converting-oauth20-service-providers-to-openidconnect":
        "https://docs.mattermost.com/onboard/convert-oauth20-service-providers-to-openidconnect.html",
    "deployment/bulk-loading": "https://docs.mattermost.com/onboard/bulk-loading-data.html",
    "deployment/ldap-group-sync": "https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html",
    "deployment/ldap-group-constrained-team-channel":
        "https://docs.mattermost.com/onboard/manage-team-channel-membership-using-ad-ldap-sync-groups.html",
    "deployment/sso-saml": "https://docs.mattermost.com/onboard/sso-saml.html",
    "deployment/sso-saml-okta": "https://docs.mattermost.com/onboard/sso-saml-okta.html",
    "deployment/sso-saml-technical": "https://docs.mattermost.com/onboard/sso-saml-technical.html",
    "deployment/sso-saml-adfs-msws2016": "https://docs.mattermost.com/onboard/sso-saml-adfs-msws2016.html",
    "deployment/ssl-client-certificate": "https://docs.mattermost.com/onboard/ssl-client-certificate.html",
    "deployment/team-channel-management": "https://docs.mattermost.com/manage/team-channel-members.html",
    "deployment/certificate-based-authentication":
        "https://docs.mattermost.com/onboard/certificate-based-authentication.html",
    "administration/devops-command-center": "https://docs.mattermost.com/guides/incident-collaboration.html",
    "administration/plugins": "https://developers.mattermost.com/integrate/admin-guide/admin-plugins-beta/", 
    "administration/migrating": "https://docs.mattermost.com/onboard/migrating-to-mattermost.html",
    "administration/user-provisioning": "https://docs.mattermost.com/onboard/user-provisioning-workflows.html",
    "administration/hipchat-migration-guidelines":
        "https://docs.mattermost.com/onboard/migrating-from-hipchat-to-mattermost.html",
    "administration/migration-announcement-email-template":
        "https://docs.mattermost.com/onboard/migration-announcement-email.html",
    "administration/generating-support-packet": "https://docs.mattermost.com/manage/generating-support-packet.html",
    "administration/mmctl-cli-tool": "https://docs.mattermost.com/manage/mmctl-command-line-tool.html",
    "administration/command-line-tools": "https://docs.mattermost.com/manage/command-line-tools.html",
    "administration/scripts": "https://docs.mattermost.com/manage/scripts.html",
    "administration/statistics": "https://docs.mattermost.com/manage/statistics.html",
    "administration/notices": "https://docs.mattermost.com/manage/in-product-notices.html",
    "administration/health-check": "https://docs.mattermost.com/manage/health-checks.html",
    "administration/announcement-banner": "https://docs.mattermost.com/manage/announcement-banner.html",
    "administration/bulk-export": "https://docs.mattermost.com/manage/bulk-export-tool.html",
    "administration/ediscovery": "https://docs.mattermost.com/comply/electronic-discovery.html",
    "administration/compliance": "https://docs.mattermost.com/comply/compliance-reporting-oversight.html",
    "administration/compliance-export": "https://docs.mattermost.com/comply/compliance-export.html",
    "administration/audit-log": "https://docs.mattermost.com/comply/audit-log.html",
    "administration/data-retention": "https://docs.mattermost.com/comply/data-retention-policy.html",
    "administration/custom-terms-of-service": "https://docs.mattermost.com/comply/custom-terms-of-service.html",
    "administration/mobile-changelog": "https://docs.mattermost.com/deploy/mobile-app-changelog.html",
    "cloud/cloud-administration/cloud-changelog": "https://docs.mattermost.com/install/cloud-changelog.html",
    "cloud/cloud-administration/cloud-compliance":
        "https://docs.mattermost.com/comply/cloud-compliance-and-oversight.html",
    "cloud/cloud-administration/compliance-export": "https://docs.mattermost.com/comply/cloud-compliance-export.html",
    "cloud/cloud-administration/data-retention-policy":
        "https://docs.mattermost.com/comply/cloud-data-retention-policy.html",
    "cloud/cloud-administration/custom-terms-of-service":
        "https://docs.mattermost.com/comply/cloud-custom-terms-of-service.html",
    "cloud/cloud-billing/cloud-billing": "https://docs.mattermost.com/manage/cloud-billing.html",
    "cloud/cloud-administration/sso-saml": "https://docs.mattermost.com/onboard/cloud-sso-saml.html",
    "cloud/cloud-administration/saml-technical": "https://docs.mattermost.com/onboard/cloud-sso-saml-technical.html",
    "cloud/cloud-reporting": "https://docs.mattermost.com/manage/cloud-reporting.html",
    "cloud/cloud-administration/site-configuration":
        "https://docs.mattermost.com/configure/cloud-site-configuration.html",
    "cloud/cloud-mobile/cloud-app-config": "https://docs.mattermost.com/deploy/mobile-appconfig.html",
    "help/apps/desktop-changelog": "https://docs.mattermost.com/install/desktop-app-changelog.html",
    "help/getting-started/welcome-to-mattermost":
        "https://docs.mattermost.com/messaging/welcome-to-mattermost-messaging.html",
    "help/getting-started/access-your-workspace": "https://docs.mattermost.com/messaging/accessing-your-workspace.html",
    "help/getting-started/signing-in": "https://docs.mattermost.com/messaging/signing-in.html",
    "help/getting-started/switch-between-teams": "https://docs.mattermost.com/messaging/switching-between-teams.html",
    "help/getting-started/about-teams-channels-messages":
        "https://docs.mattermost.com/messaging/about-teams-channels-messages.html",
    "help/getting-started/log-out": "https://docs.mattermost.com/messaging/logging-out.html",
    "help/getting-started/searching": "https://docs.mattermost.com/messaging/searching-in-mattermost.html",
    "help/getting-started/creating-teams": "https://docs.mattermost.com/messaging/creating-teams.html",
    "help/settings/team-settings": "https://docs.mattermost.com/messaging/team-settings.html",
    "help/getting-started/organizing-conversations": "https://docs.mattermost.com/messaging/managing-channels.html",
    "help/getting-started/organizing": "https://docs.mattermost.com/messaging/organizing-mattermost.html",
    "help/settings/channel-settings": "https://docs.mattermost.com/messaging/channel-settings.html",
    "help/getting-started/managing-members": "https://docs.mattermost.com/messaging/managing-members.html",
    "help/getting-started/setting-your-status-availability":
        "https://docs.mattermost.com/messaging/setting-your-status-availability.html",
    "help/getting-started/configuring-notifications":
        "https://docs.mattermost.com/messaging/configuring-notifications.html",
    "help/getting-started/organizing-your-sidebar":
        "https://docs.mattermost.com/messaging/organizing-your-sidebar.html",
    "help/messaging/sending-messages": "https://docs.mattermost.com/messaging/sending-receiving-messages.html",
    "help/messaging/organizing-conversations": "https://docs.mattermost.com/messaging/organizing-conversations.html",
    "help/messaging/organizing-conversations#known-issues":
        "https://docs.mattermost.com/messaging/organizing-conversations.html#known-issues",
    "help/messaging/formatting-text": "https://docs.mattermost.com/messaging/formatting-text.html",
    "help/messaging/emoji": "https://docs.mattermost.com/messaging/using-emoji.html",
    "help/messaging/mentioning-teammates": "https://docs.mattermost.com/messaging/mentioning-teammates.html",
    "help/messaging/attaching-files": "https://docs.mattermost.com/messaging/sharing-files.html",
    "help/messaging/executing-commands": "https://docs.mattermost.com/messaging/executing-slash-commands.html",
    "help/messaging/flagging-messages": "https://docs.mattermost.com/messaging/saving-messages.html",
    "help/messaging/pinning-messages": "https://docs.mattermost.com/messaging/pinning-messages.html",
    "help/messaging/keyboard-shortcuts": "https://docs.mattermost.com/messaging/keyboard-shortcuts.html",
    "help/settings/custom-emoji": "https://docs.mattermost.com/messaging/using-custom-emoji.html",
    "help/settings/account-settings": "https://docs.mattermost.com/messaging/managing-account-settings.html",
    "help/settings/theme-colors": "https://docs.mattermost.com/messaging/customizing-theme-colors.html",
    "help/settings/desktop-app-options": "https://docs.mattermost.com/messaging/managing-desktop-app-options.html",
    "help/settings/manage-servers": "https://docs.mattermost.com/messaging/managing-desktop-app-servers.html",
    "help/getting-started/accessibility": "https://docs.mattermost.com/messaging/keyboard-accessibility.html",
    "help/settings/integration-settings":
        "https://docs.mattermost.com/messaging/extending-messaging-with-integrations.html",
    "help/getting-started/install-desktop-app":
        "https://docs.mattermost.com/install/installing-mattermost-desktop-app.html",
    "help/getting-started/light-install": "https://docs.mattermost.com/getting-started/light-install.html",
     "incident-collaboration/playbook-planning": 
        "https://docs.mattermost.com/incident-collaboration/setting-up-playbooks.html",
     "incident-collaboration/launching-playbooks": 
        "https://docs.mattermost.com/incident-collaboration/running-playbooks.html",
     "incident-collaboration/review-and-refine": 
        "https://docs.mattermost.com/incident-collaboration/refining-and-improving.html",
     "incident-collaboration/overview": "https://docs.mattermost.com/playbooks/refining-and-improving.html",
     "incident-collaboration/getting-started": "https://docs.mattermost.com/playbooks/getting-started.html",
     "incident-collaboration/setting-up-playbooks": "https://docs.mattermost.com/playbooks/setting-up-playbooks.html",
     "incident-collaboration/running-playbooks": "https://docs.mattermost.com/playbooks/running-playbooks.html",
     "incident-collaboration/refining-and-improving": 
         "https://docs.mattermost.com/playbooks/refining-and-improving.html",
    "process/help-wanted": "https://handbook.mattermost.com/contributors/contributors/help-wanted",
    "process/sg_rest_markup":
        "https://handbook.mattermost.com/operations/operations/company-processes/publishing/publishing-guidelines"
        "/voice-tone-and-writing-style-guidelines/documentation-style-guide#document-structure",
    "process/security-release":
        "https://handbook.mattermost.com/operations/research-and-development/product/release-process/security-release",
    "process/community-overview": "https://handbook.mattermost.com/contributors/contributors/community",
    "process/handbook": "https://handbook.mattermost.com/company/about-mattermost",
    "process/release-faq":
        "https://handbook.mattermost.com/operations/research-and-development/product/release-process/release-overview",
    "process/release-tips":
        "https://handbook.mattermost.com/operations/research-and-development/product/release-process/release-tips",
    "process/sg_general-guidelines":
        "https://handbook.mattermost.com/operations/operations/company-processes/publishing/publishing-guidelines"
        "/voice-tone-and-writing-style-guidelines/documentation-style-guide#document-structure",
    "process/community-guidelines":
        "https://handbook.mattermost.com/contributors/contributors/community-playbook/",
    "process/feature-release":
        "https://handbook.mattermost.com/operations/research-and-development/product/release-process/feature-release",
    "process/security": "https://handbook.mattermost.com/operations/operations/company-policies/security-policies",
    "process/engineer-expectations":
        "https://handbook.mattermost.com/operations/workplace/people/working-at-mattermost/onboarding/engineer"
        "-onboarding",
    "process/product-manager-hiring":
        "https://handbook.mattermost.com/contributors/join-us/recruiting-cadences/product-manager-hiring",
    "process/new-bug-tickets":
        "https://handbook.mattermost.com/operations/research-and-development/product/development-process/new-bug"
        "-tickets",
    "process/sg_grammar-spelling-mechanics":
        "https://handbook.mattermost.com/operations/operations/company-processes/publishing/publishing-guidelines"
        "/voice-tone-and-writing-style-guidelines/documentation-style-guide#document-structure",
    "process/sg_document-structure":
        "https://handbook.mattermost.com/operations/operations/company-processes/publishing/publishing-guidelines"
        "/voice-tone-and-writing-style-guidelines/documentation-style-guide#document-structure",
    "process/release-scorecard-definitions":
        "https://handbook.mattermost.com/operations/research-and-development/product/release-process/release"
        "-scorecard-definitions",
    "process/software-requirements":
        "https://handbook.mattermost.com/operations/research-and-development/product/development-process/software"
        "-requirements",
    "process/mobile-release-process":
        "https://handbook.mattermost.com/operations/research-and-development/product/release-process/mobile-release",
    "process/documentation-UItext-guidelines":
        "https://handbook.mattermost.com/operations/research-and-development/product/development-process/user"
        "-interface-text-guidelines",
    "process/bug-fix-release":
        "https://handbook.mattermost.com/operations/research-and-development/product/release-process/bug-fix-release",
    "process/deprecated-features":
        "https://handbook.mattermost.com/operations/research-and-development/product/development-process/deprecated"
        "-features",
    "process/dot-release":
        "https://handbook.mattermost.com/operations/research-and-development/product/release-process/dot-release",
    "process/end-user-documentation":
        "https://handbook.mattermost.com/operations/operations/company-processes/publishing/publishing-guidelines"
        "/voice-tone-and-writing-style-guidelines/documentation-style-guide#document-structure",
    "process/bug-severity-guidelines":
        "https://handbook.mattermost.com/operations/research-and-development/product/development-process/new-bug"
        "-tickets/bug-severity-guidelines",
    "process/accepting-pull-request":
        "https://handbook.mattermost.com/contributors/contributors/help-wanted",
    "process/pm-faq":
        "https://handbook.mattermost.com/operations/research-and-development/product/product-management-team-handbook"
        "#frequently-asked-questions-faq",
    "process/product-manager":
        "https://handbook.mattermost.com/contributors/join-us/staff-recruiting/product-manager-hiring",
    "process/partner-programs":
        "https://handbook.mattermost.com/operations/sales/partner-programs",
    "process/overview":
        "https://handbook.mattermost.com/operations/research-and-development/product/development-process",
    "mobile/mobile-hpns": "https://docs.mattermost.com/deploy/mobile-hpns.html"

}

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Mattermost'
copyright = '2015-2021 Mattermost'
author = 'Mattermost'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# version = '5.37'
# The full version, including alpha/beta/rc tags.
# release = '5.37'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['archive/*']

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

html_baseurl = 'https://docs.mattermost.com/'

# Global variables available to all templates
html_context = {
    # Enable google analytics
    'googleanalytics_id': 'UA-67846571-2',
    'googleanalytics_enabled': True,

    # Enable the "Edit in GitHub link within the header of each page.
    'display_github': True,

    # Set the following variables to generate the resulting github URL for each page. Format Template:
    # https://{{github_host|default("github.com") }}
    # /{{ github_user }}/{{ github_repo }}/blob/{{ github_version }}{{conf_py_path }}{{ pagename }}{{ suffix }}
    'github_user': 'mattermost',
    'github_repo': 'docs',
    'github_version': 'master/source/',

    'css_files': []
}

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': -1,  # Allow unlimited depth in navigation
    'includehidden': False,
    'titles_only': False
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', 'theme.css', 'myscript.js']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
html_extra_path = ['_static/robots.txt']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {
    'index': 'index.html',
    '404': '404.html'
}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'Mattermostdoc'
