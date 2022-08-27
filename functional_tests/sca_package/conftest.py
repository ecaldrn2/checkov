from typing import Dict, Any, List

import pytest

from checkov.common.bridgecrew.bc_source import SourceType
from checkov.common.bridgecrew.platform_integration import BcPlatformIntegration, bc_integration


@pytest.fixture()
def mock_bc_integration() -> BcPlatformIntegration:
    bc_integration.bc_api_key = "abcd1234-abcd-1234-abcd-1234abcd1234"
    bc_integration.setup_bridgecrew_credentials(
        repo_id="bridgecrewio/checkov",
        skip_fixes=True,
        skip_download=True,
        source=SourceType("Github", False),
        source_version="1.0",
        repo_branch="master",
    )
    return bc_integration


@pytest.fixture()
def scan_result() -> List[Dict[str, Any]]:
    return [
        {
            "repository": "/path/to/requirements.txt",
            "passed": True,
            "packages": [
                {
                    "type": "python",
                    "name": "requests",
                    "version": "2.26.0",
                    "path": "/path/to/requirements.txt",
                },
                {
                    "type": "python",
                    "name": "django",
                    "version": "1.2",
                    "path": "/path/to/requirements.txt",
                },
                {
                    "type": "python",
                    "name": "flask",
                    "version": "0.6",
                    "path": "/path/to/requirements.txt",
                },
            ],
            "complianceIssues": None,
            "complianceDistribution": {"critical": 0, "high": 0, "medium": 0, "low": 0, "total": 0},
            "vulnerabilities": [
                {
                    "id": "CVE-2019-19844",
                    "status": "fixed in 3.0.1, 2.2.9, 1.11.27",
                    "cvss": 9.8,
                    "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
                    "description": "Django before 1.11.27, 2.x before 2.2.9, and 3.x before 3.0.1 allows account takeover. A suitably crafted email address (that is equal to an existing user\\'s email address after case transformation of Unicode characters) would allow an attacker to be sent a password reset token for the matched user account. (One mitigation in the new releases is to send password reset tokens only to the registered user email address.)",
                    "severity": "critical",
                    "packageName": "django",
                    "packageVersion": "1.2",
                    "link": "https://nvd.nist.gov/vuln/detail/CVE-2019-19844",
                    "riskFactors": ["Attack complexity: low", "Attack vector: network", "Critical severity", "Has fix"],
                    "impactedVersions": ["<1.11.27"],
                    "publishedDate": "2019-12-18T20:15:00+01:00",
                    "discoveredDate": "2019-12-18T19:15:00Z",
                    "fixDate": "2019-12-18T20:15:00+01:00",
                },
                {
                    "id": "CVE-2016-6186",
                    "status": "fixed in 1.9.8, 1.8.14",
                    "cvss": 6.1,
                    "vector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N",
                    "description": "Cross-site scripting (XSS) vulnerability in the dismissChangeRelatedObjectPopup function in contrib/admin/static/admin/js/admin/RelatedObjectLookups.js in Django before 1.8.14, 1.9.x before 1.9.8, and 1.10.x before 1.10rc1 allows remote attackers to inject arbitrary web script or HTML via vectors involving unsafe usage of Element.innerHTML.",
                    "severity": "medium",
                    "packageName": "django",
                    "packageVersion": "1.2",
                    "link": "https://nvd.nist.gov/vuln/detail/CVE-2016-6186",
                    "riskFactors": [
                        "Attack complexity: low",
                        "Attack vector: network",
                        "Exploit exists",
                        "Has fix",
                        "Medium severity",
                    ],
                    "impactedVersions": ["<=1.8.13"],
                    "publishedDate": "2016-08-05T17:59:00+02:00",
                    "discoveredDate": "2016-08-05T15:59:00Z",
                    "fixDate": "2016-08-05T17:59:00+02:00",
                },
                {
                    "id": "CVE-2016-7401",
                    "status": "fixed in 1.9.10, 1.8.15",
                    "cvss": 7.5,
                    "vector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N",
                    "description": "The cookie parsing code in Django before 1.8.15 and 1.9.x before 1.9.10, when used on a site with Google Analytics, allows remote attackers to bypass an intended CSRF protection mechanism by setting arbitrary cookies.",
                    "severity": "high",
                    "packageName": "django",
                    "packageVersion": "1.2",
                    "link": "https://nvd.nist.gov/vuln/detail/CVE-2016-7401",
                    "riskFactors": ["High severity", "Attack complexity: low", "Attack vector: network", "Has fix"],
                    "impactedVersions": ["<=1.8.14"],
                    "publishedDate": "2016-10-03T20:59:00+02:00",
                    "discoveredDate": "2016-10-03T18:59:00Z",
                    "fixDate": "2016-10-03T20:59:00+02:00",
                },
                {
                    "id": "CVE-2021-33203",
                    "status": "fixed in 3.2.4, 3.1.12, 2.2.24",
                    "cvss": 4.9,
                    "vector": "CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N",
                    "description": "Django before 2.2.24, 3.x before 3.1.12, and 3.2.x before 3.2.4 has a potential directory traversal via django.contrib.admindocs. Staff members could use the TemplateDetailView view to check the existence of arbitrary files. Additionally, if (and only if) the default admindocs templates have been customized by application developers to also show file contents, then not only the existence but also the file contents would have been exposed. In other words, there is directory traversal outside of the template root directories.",
                    "severity": "medium",
                    "packageName": "django",
                    "packageVersion": "1.2",
                    "link": "https://nvd.nist.gov/vuln/detail/CVE-2021-33203",
                    "riskFactors": [
                        "Attack complexity: low",
                        "Attack vector: network",
                        "Has fix",
                        "Medium severity",
                        "Recent vulnerability",
                    ],
                    "impactedVersions": ["<2.2.24"],
                    "publishedDate": "2021-06-08T20:15:00+02:00",
                    "discoveredDate": "2021-06-08T18:15:00Z",
                    "fixDate": "2021-06-08T20:15:00+02:00",
                },
                {
                    "id": "CVE-2019-1010083",
                    "status": "fixed in 1.0",
                    "cvss": 7.5,
                    "vector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H",
                    "description": "The Pallets Project Flask before 1.0 is affected by: unexpected memory usage. The impact is: denial of service. The attack vector is: crafted encoded JSON data. The fixed version is: 1. NOTE: this may overlap CVE-2018-1000656.",
                    "severity": "high",
                    "packageName": "flask",
                    "packageVersion": "0.6",
                    "link": "https://nvd.nist.gov/vuln/detail/CVE-2019-1010083",
                    "riskFactors": [
                        "Attack complexity: low",
                        "Attack vector: network",
                        "DoS",
                        "Has fix",
                        "High severity",
                    ],
                    "impactedVersions": ["<1.0"],
                    "publishedDate": "2019-07-17T16:15:00+02:00",
                    "discoveredDate": "2019-07-17T14:15:00Z",
                    "fixDate": "2019-07-17T16:15:00+02:00",
                },
                {
                    "id": "CVE-2018-1000656",
                    "status": "fixed in 0.12.3",
                    "cvss": 7.5,
                    "vector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H",
                    "description": "The Pallets Project flask version Before 0.12.3 contains a CWE-20: Improper Input Validation vulnerability in flask that can result in Large amount of memory usage possibly leading to denial of service. This attack appear to be exploitable via Attacker provides JSON data in incorrect encoding. This vulnerability appears to have been fixed in 0.12.3. NOTE: this may overlap CVE-2019-1010083.",
                    "severity": "high",
                    "packageName": "flask",
                    "packageVersion": "0.6",
                    "link": "https://nvd.nist.gov/vuln/detail/CVE-2018-1000656",
                    "riskFactors": [
                        "Attack complexity: low",
                        "Attack vector: network",
                        "DoS",
                        "Has fix",
                        "High severity",
                    ],
                    "impactedVersions": ["<0.12.3"],
                    "publishedDate": "2018-08-20T21:31:00+02:00",
                    "discoveredDate": "2018-08-20T19:31:00Z",
                    "fixDate": "2018-08-20T21:31:00+02:00",
                },
            ],
            "vulnerabilityDistribution": {"critical": 1, "high": 3, "medium": 2, "low": 0, "total": 6},
            "license_statuses": [
                {
                    "packageName": "django",
                    "packageVersion": "1.2",
                    "packageLang": "python",
                    "license": "OSI_BDS",
                    "status": "COMPLIANT",
                    "policy": "BC_LIC_1"
                },
                {
                    "packageName": "flask",
                    "packageVersion": "0.6",
                    "packageLang": "python",
                    "license": "OSI_APACHE",
                    "status": "COMPLIANT",
                    "policy": "BC_LIC_1"
                },
                {
                    "packageName": "flask",
                    "packageVersion": "0.6",
                    "packageLang": "python",
                    "license": "DUMMY_OTHER_LICENSE",  # not a real license. it is just for test a package with 2 licenses
                    "status": "OPEN",
                    "policy": "BC_LIC_1"
                },
                {
                    "packageName": "requests",
                    "packageVersion": "2.26.0",
                    "packageLang": "python",
                    "license": "OSI_APACHE",
                    "status": "COMPLIANT",
                    "policy": "BC_LIC_1"
                }
            ],
        },
        {
            "repository": "/path/to/sub/requirements.txt",
            "passed": True,
            "packages": [
                {
                    "type": "python",
                    "name": "requests",
                    "version": "2.26.0",
                    "path": "/path/to/sub/requirements.txt",
                }
            ],
            "complianceIssues": None,
            "complianceDistribution": {"critical": 0, "high": 0, "medium": 0, "low": 0, "total": 0},
            "vulnerabilities": None,
            "vulnerabilityDistribution": {"critical": 0, "high": 0, "medium": 0, "low": 0, "total": 0},
            "license_statuses": [
                {
                    "packageName": "requests",
                    "packageVersion": "2.26.0",
                    "packageLang": "python",
                    "license": "OSI_APACHE",
                    "status": "COMPLIANT",
                    "policy": "BC_LIC_1"
                }
            ],
        },
        {
            "repository": "/path/to/go.sum",
            "passed": True,
            "packages": [
                {
                    "type": "go",
                    "name": "github.com/miekg/dns",
                    "version": "v1.1.41",
                    "path": "/path/to/go.sum",
                },
                {
                    "type": "go",
                    "name": "golang.org/x/crypto",
                    "version": "v0.0.0-20200622213623-75b288015ac9",
                    "path": "/path/to/go.sum",
                },
                {
                    "type": "go",
                    "name": "github.com/dgrijalva/jwt-go",
                    "version": "v3.2.0",
                    "path": "/path/to/go.sum",
                },
                {
                    "type": "go",
                    "name": "github.com/prometheus/client_model",
                    "version": "v0.0.0-20190129233127-fd36f4220a90",
                    "path": "/path/to/go.sum",
                }
            ],
            "complianceIssues": None,
            "complianceDistribution": {"critical": 0, "high": 0, "medium": 0, "low": 0, "total": 0},
            "vulnerabilities": [
                {
                    "id": "CVE-2020-29652",
                    "status": "fixed in v0.0.0-20201216223049-8b5274cf687f",
                    "cvss": 7.5,
                    "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H",
                    "description": "A nil pointer dereference in the golang.org/x/crypto/ssh component through v0.0.0-20201203163018-be400aefbc4c for Go allows remote attackers to cause a denial of service against SSH servers.",
                    "severity": "high",
                    "packageName": "golang.org/x/crypto",
                    "packageVersion": "v0.0.0-20200622213623-75b288015ac9",
                    "link": "https://nvd.nist.gov/vuln/detail/CVE-2020-29652",
                    "riskFactors": [
                        "Has fix",
                        "High severity",
                        "Attack complexity: low",
                        "Attack vector: network",
                        "DoS",
                    ],
                    "impactedVersions": ["<v0.0.0-20201216223049-8b5274cf687f"],
                    "publishedDate": "2020-12-17T06:15:00+01:00",
                    "discoveredDate": "2020-12-17T05:15:00Z",
                    "fixDate": "2020-12-17T06:15:00+01:00",
                },
                {
                    "id": "CVE-2020-26160",
                    "status": "fixed in v4.0.0-preview1",
                    "cvss": 7.7,
                    "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N",
                    "description": 'jwt-go before 4.0.0-preview1 allows attackers to bypass intended access restrictions in situations with []string{} for m[\\"aud\\"] (which is allowed by the specification). Because the type assertion fails, \\"\\" is the value of aud. This is a security problem if the JWT token is presented to a service that lacks its own audience check.',
                    "severity": "high",
                    "packageName": "github.com/dgrijalva/jwt-go",
                    "packageVersion": "v3.2.0",
                    "link": "https://nvd.nist.gov/vuln/detail/CVE-2020-26160",
                    "riskFactors": ["High severity", "Attack complexity: low", "Attack vector: network", "Has fix"],
                    "impactedVersions": ["<v4.0.0-preview1"],
                    "publishedDate": "2020-09-30T20:15:00+02:00",
                    "discoveredDate": "2020-09-30T18:15:00Z",
                    "fixDate": "2020-09-30T20:15:00+02:00",
                },
            ],
            "vulnerabilityDistribution": {"critical": 0, "high": 2, "medium": 0, "low": 0, "total": 2},
        },
    ]