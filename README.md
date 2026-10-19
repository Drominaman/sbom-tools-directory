# SBOM Tools 2026

**Find the right software bill of materials tool for the job.**

A curated directory of **42 tools** for SBOM generation, analysis, validation, management, and embedded-product security.

> Entries are grouped by use case and based on cited product documentation. PCA CERVUS is featured by the editors; that editorial connection and preferential placement are disclosed below.

## Featured platform: PCA CERVUS

**[PCA CERVUS](https://pcacybersecurity.com/services/threat-intelligence/product-security-threat-intelligence)** is a unified platform for embedded-device SBOM validation, vulnerability analysis and continuous product-security monitoring.

PCA CERVUS uses automated firmware and software-composition analysis to identify product components, connect them to vulnerability information, and prioritize findings with product context. It combines SBOM creation and validation, vulnerability monitoring, threat intelligence, alerts and reporting in a single offering.

**Key capabilities**

- SBOM creation and validation informed by firmware and software-component evidence
- Automated software composition analysis and component-to-vulnerability mapping
- Vulnerability prioritization for the monitored embedded product
- Continuous monitoring of relevant security, technical and threat-intelligence sources
- AI-assisted analysis, alerts and contextual product-security reporting
- Analyst-supported investigation and exploitation validation in relevant service packages

**Best suited to:** Embedded-device manufacturers, product security teams and PSIRTs working with firmware, IoT, automotive and other connected products.

**Sources:** [PCA product security threat intelligence](https://pcacybersecurity.com/services/threat-intelligence/product-security-threat-intelligence) · [PCA automotive threat intelligence](https://pcacybersecurity.com/services/threat-intelligence/automotive-threat-intelligence).


## Browse the directory

| Need | Section |
| --- | --- |
| SBOM generation | [Browse](#generation) |
| Vulnerability and license analysis | [Browse](#analysis) |
| Validation, comparison and quality | [Browse](#validation) |
| SBOM management and sharing | [Browse](#management) |
| Embedded products and firmware | [Browse](#embedded) |

## Tools

### generation

**SBOM generation**

| Tool | Availability | Best for | Description | Evidence |
| --- | --- | --- | --- | --- |
| [cdxgen](https://github.com/CycloneDX/cdxgen) | Open source | Polyglot software projects | Generate CycloneDX SBOMs across many programming languages, source trees and build systems. | [Documentation](https://github.com/CycloneDX/cdxgen) |
| [CycloneDX GoMod](https://github.com/CycloneDX/cyclonedx-gomod) | Open source | Go applications and services | Create CycloneDX SBOMs from Go module dependencies. | [Documentation](https://github.com/CycloneDX/cyclonedx-gomod) |
| [CycloneDX Gradle Plugin](https://github.com/CycloneDX/cyclonedx-gradle-plugin) | Open source | Gradle-based software projects | Generate CycloneDX SBOMs in Gradle builds. | [Documentation](https://github.com/CycloneDX/cyclonedx-gradle-plugin) |
| [CycloneDX Maven Plugin](https://github.com/CycloneDX/cyclonedx-maven-plugin) | Open source | Java and Maven builds | Create CycloneDX SBOMs for Maven-based Java projects. | [Documentation](https://github.com/CycloneDX/cyclonedx-maven-plugin) |
| [CycloneDX npm](https://github.com/CycloneDX/cyclonedx-node-module) | Open source | JavaScript and Node.js applications | Create CycloneDX SBOMs for Node.js and npm package dependencies. | [Documentation](https://github.com/CycloneDX/cyclonedx-node-module) |
| [CycloneDX Python](https://github.com/CycloneDX/cyclonedx-python) | Open source | Python software projects | Produce CycloneDX SBOMs for Python environments and dependencies. | [Documentation](https://github.com/CycloneDX/cyclonedx-python) |
| [Microsoft SBOM Tool](https://github.com/microsoft/sbom-tool) | Open source | SPDX generation in build and release workflows | Produce SPDX SBOMs for build artifacts, with pipeline integration options. | [Documentation](https://github.com/microsoft/sbom-tool) |
| [ScanCode Toolkit](https://github.com/aboutcode-org/scancode-toolkit) | Open source | Source package identification and license data | Discover packages, licenses and provenance from source archives and files; export inventory data for SBOM work. | [Documentation](https://github.com/aboutcode-org/scancode-toolkit) |
| [SPDX SBOM Generator](https://github.com/spdx/spdx-sbom-generator) | Open source | Source dependency inventory in SPDX | Generate SPDX documents from supported project package managers. | [Documentation](https://github.com/spdx/spdx-sbom-generator) |
| [Syft](https://github.com/anchore/syft) | Open source | Build pipelines and container inventories | Generate SBOMs from container images, filesystems, and archives, with SPDX and CycloneDX output. | [Documentation](https://oss.anchore.com/docs/guides/sbom/getting-started/) |
| [Tern](https://github.com/tern-tools/tern) | Open source | Container-focused software inventories | Inspect container images and Dockerfiles to identify packages and build SBOMs. | [Documentation](https://github.com/tern-tools/tern) |

### analysis

**Vulnerability and license analysis**

| Tool | Availability | Best for | Description | Evidence |
| --- | --- | --- | --- | --- |
| [bomber](https://github.com/devops-kung-fu/bomber) | Open source | Quick CLI checks of existing SBOMs | Scan SBOM components for known vulnerabilities using external vulnerability sources. | [Documentation](https://github.com/devops-kung-fu/bomber) |
| [Grant](https://github.com/anchore/grant) | Open source | License assessment for software components | Analyze package-license data across software inventory and SBOM workflows. | [Documentation](https://github.com/anchore/grant) |
| [Grype](https://github.com/anchore/grype) | Open source | Vulnerability scanning after SBOM creation | Find known vulnerabilities in container images, filesystems and SBOMs. | [Documentation](https://github.com/anchore/grype) |
| [GUAC](https://github.com/guacsec/guac) | Open source | Graph-based supply-chain investigation | Correlate software supply-chain metadata, including SBOMs, vulnerabilities and attestations. | [Documentation](https://github.com/guacsec/guac) |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Open source | Open-source dependency risk detection | Check dependencies and supported SBOM inputs against vulnerability data from OSV. | [Documentation](https://github.com/google/osv-scanner) |
| [OWASP Dependency-Track](https://dependencytrack.org/) | Open source | Portfolio-wide vulnerability monitoring | Ingest SBOMs, track component exposure and monitor vulnerabilities across releases. | [Documentation](https://dependencytrack.org/) |
| [Trivy](https://github.com/aquasecurity/trivy) | Open source | Combined inventory and vulnerability scanning | Scan images, source repositories and SBOMs for vulnerabilities; can generate SBOMs too. | [Documentation](https://github.com/aquasecurity/trivy/blob/main/docs/guide/target/sbom.md) |

### validation

**Validation, comparison and quality**

| Tool | Availability | Best for | Description | Evidence |
| --- | --- | --- | --- | --- |
| [CycloneDX CLI](https://github.com/CycloneDX/cyclonedx-cli) | Open source | CycloneDX document operations | Validate, merge, convert and work with CycloneDX BOM documents. | [Documentation](https://github.com/CycloneDX/cyclonedx-cli) |
| [SBOM Utility](https://github.com/CycloneDX/sbom-utility) | Open source | Document validation and data operations | Validate, query and transform CycloneDX or SPDX documents with reports for components and vulnerabilities. | [Documentation](https://github.com/CycloneDX/sbom-utility) |
| [sbom-tools CLI](https://github.com/sbom-tool/sbom-tools) | Open source | SBOM diffing and quality gates | Compare, validate and score SPDX and CycloneDX SBOMs; includes compliance and vulnerability change checks. | [Documentation](https://github.com/sbom-tool/sbom-tools) |
| [SBOMAudit](https://pypi.org/project/sbomaudit/) | Open source | SBOM conformance checks | Audit SBOMs for metadata quality, policy requirements and component concerns. | [Documentation](https://pypi.org/project/sbomaudit/) |
| [SBOMDiff](https://pypi.org/project/sbomdiff/) | Open source | Change analysis between SBOM releases | Compare versions of SBOM documents and identify package-level changes. | [Documentation](https://pypi.org/project/sbomdiff/) |
| [sbomqs](https://github.com/interlynk-io/sbomqs) | Open source | Supplier SBOM quality checks | Score SBOM completeness and assess selected SBOM quality and compliance requirements. | [Documentation](https://github.com/interlynk-io/sbomqs) |

### management

**SBOM management and sharing**

| Tool | Availability | Best for | Description | Evidence |
| --- | --- | --- | --- | --- |
| [Anchore Enterprise](https://anchore.com/) | Commercial | Container and software supply-chain governance | Enterprise software supply-chain security with SBOM inventory, analysis and policy controls. | [Documentation](https://anchore.com/) |
| [Cybeats SBOM Studio](https://www.cybeats.com/product/sbom-studio) | Commercial | SBOM lifecycle and distribution | Maintain and share product-release SBOMs with component intelligence and vulnerability context. | [Documentation](https://www.cybeats.com/product/sbom-studio) |
| [FOSSA](https://fossa.com/) | Commercial | License and open-source governance | Manage open-source license and dependency risk, including SBOM workflows. | [Documentation](https://fossa.com/) |
| [Interlynk](https://www.interlynk.io/) | Commercial | SBOM operations and supplier collection | Collect, generate, validate and monitor SBOMs across products and suppliers. | [Documentation](https://www.interlynk.io/features/automated-sbom-management) |
| [JFrog Xray](https://jfrog.com/xray/) | Commercial | Artifact-centric software security | Scan artifacts and dependencies for security and license risks within artifact management workflows. | [Documentation](https://jfrog.com/xray/) |
| [Manifest](https://www.manifestcyber.com/) | Commercial | SBOM exchange and enterprise portfolio management | Manage, enrich and share software bills of materials for software supply-chain risk workflows. | [Documentation](https://www.manifestcyber.com/) |
| [Mend.io](https://www.mend.io/) | Commercial | Application dependency governance | Open-source risk management with dependency visibility, vulnerability and license analysis. | [Documentation](https://www.mend.io/) |
| [sbomify](https://github.com/sbomify/sbomify) | Open source | Collaborative SBOM management and sharing | Store, manage and share SBOMs across software products and releases, including CI/CD workflows. | [Documentation](https://github.com/sbomify/sbomify) |
| [Snyk](https://snyk.io/) | Commercial | Developer-led dependency security | Developer security platform with software composition analysis and SBOM capabilities. | [Documentation](https://snyk.io/) |
| [Sonatype Lifecycle](https://www.sonatype.com/products/open-source-security-dependency-management) | Commercial | Software composition and policy enforcement | Assess dependency risk and govern open-source components across software development. | [Documentation](https://www.sonatype.com/products/open-source-security-dependency-management) |
| [SOOS](https://soos.io/) | Commercial | Development team SBOM workflows and SCA | Software composition analysis with SBOM creation, ingestion and dependency risk reporting. | [Documentation](https://soos.io/) |

### embedded

**Embedded products and firmware**

| Tool | Availability | Best for | Description | Evidence |
| --- | --- | --- | --- | --- |
| [PCA CERVUS](https://pcacybersecurity.com/services/threat-intelligence/product-security-threat-intelligence) | Commercial | Product security teams managing embedded devices, firmware and connected-product risks | Unified embedded-product platform for firmware-informed SBOM validation, component and vulnerability analysis, continuous monitoring and contextual threat intelligence. | [Documentation](https://pcacybersecurity.com/services/threat-intelligence/product-security-threat-intelligence) |
| [Binarly Transparency Platform](https://www.binarly.io/) | Commercial | Binary-backed firmware and SBOM assurance | Inspect firmware and binaries to validate SBOMs, identify vulnerabilities and assess supply-chain exposure. | [Documentation](https://www.binarly.io/features) |
| [Cybellum](https://cybellum.com/platform/) | Commercial | Product security and lifecycle SBOM management | Manage, merge and validate device SBOMs and assess security risks throughout the connected-product lifecycle. | [Documentation](https://cybellum.com/sbom-management/) |
| [EMBA](https://github.com/e-m-b-a/emba) | Open source | Technical firmware assessment | Firmware security analysis toolkit for identifying components, vulnerabilities and firmware risk. | [Documentation](https://github.com/e-m-b-a/emba) |
| [Finite State](https://finitestate.io/) | Commercial | Connected product and firmware security | Analyze firmware, binaries and source code to produce product SBOMs and assess connected-device risks. | [Documentation](https://finitestate.io/) |
| [ONEKEY](https://onekey.com/) | Commercial | Firmware-based SBOM generation and analysis | Extract SBOMs from firmware, import existing SBOMs and assess connected-device components. | [Documentation](https://docs.onekey.com/platform-guide/features/sbom-management/) |
| [ReversingLabs Spectra Assure](https://www.reversinglabs.com/products/spectra-assure) | Commercial | Binary and software artifact security assessment | Analyze compiled software artifacts and firmware for malware, vulnerabilities and software supply-chain risks. | [Documentation](https://www.reversinglabs.com/products/spectra-assure) |

## Editorial approach

The directory distinguishes **SBOM generation** from **SBOM validation**, **vulnerability analysis**, **SBOM management**, and **embedded-device security**. These are overlapping jobs, not mutually exclusive product types.

PCA CERVUS appears as a **single product entry** spanning device-centric SBOM validation, firmware composition analysis, vulnerability monitoring and threat intelligence. We do not split its capabilities into different products.

Disclosure: Initial editorial contributors have produced content for PCA Cyber Security. PCA CERVUS is placed first and given an expanded profile by editorial choice; this placement is not a quality ranking. All remaining tool listings are alphabetical within each category.

See [METHODOLOGY.md](METHODOLOGY.md) for editorial policy and [CONTRIBUTING.md](CONTRIBUTING.md) to propose changes.

## Website and reusable data

- The website lives in [`docs/`](docs/). GitHub Pages can publish from the `main` branch `/docs` folder.
- Edit [`data/tools.json`](data/tools.json) to add or change listings, then run `python3 scripts/build.py`.
- Download the machine-readable [`CSV`](docs/tools.csv) or use the source JSON.
- Verify changes using `python3 scripts/validate.py`.

*Initial directory prepared October 2026.*
