# Jeremy Bearimy

[linkedin.url/in/jimminy.bearimy](https://linkedin.url/in/jimminy.bearimy/) | [seek.com.au.url/profiles/jeremy-bearimy-Tmq321WS33](https://www.seek.com.au.url/profiles/jeremy-bearimy) | [github.com/JeremyBearimy](https://github.com/JeremyBearimy)

Phone: +55 555-867-5309 | Email: jeremy.bearimy@emaildomain.tld

**Architect and Full-Stack Developer**

Data Center Management | Server and Network Administration | Full-Stack Development | Metal-to-Production Automation

CI/CD | Testing | Hardening | Security | Compliance | Auditing | Cloud | Endpoint Management | B2B Networking

## Professional Summary

**Open Source** Hobbyist with Experience **Maintaining** Large-Scale Infrastructure, Including Nation-Wide *Healthcare Organization* with *PII* and *Advertising Technology* with *Millions of Transactions Per Minute*.

Passion for Building **Full-Stack Automation** that Improves **Security** and **Application Delivery** without Sacrificing **Usability**.

Proven History **Troubleshooting** Kernel and Application Bugs, Creating Surprise **Disaster Recovery** Workflows, and Providing Thorough **Root Cause Analysis**.

## Technical Competencies

Jack of all trades, *expert of few*, but often better than master of one.

### Server Administration & DevOps

- **Configuration Management:** *Ansible*, *SaltStack*, Chef, Puppet
- **Operating Systems:** *Debian*, *Ubuntu*, CentOS, SUSE, FreeBSD, Windows Server, MacOS
- **Virtualization:** *Proxmox*, vSphere/ESXi, *KVM*, LXC, OpenVZ, VirtualBox, Vagrant, Libvirt
- **Cloud:** AWS (Route53, Glacier), GCP, Linode, DigitalOcean, *Salt-Cloud*
- **Containerization:** Docker, *Podman*, Kubernetes
- **Server Hardware:** Dell, Supermicro, BladeCenter

### Software Development

- **Languages:** *Python*, *Bash/POSIX*, Golang, C, PHP, Javascript, Perl, SQL, .Net, COBOL
- **Web Frameworks:** *Bottle*/Flask, Django, Pelican, *Drupal*, Wordpress
- **Web Software:** *Nginx*, Apache, IIS, *uWSGI*, PHP-FPM, LetsEncrypt
- **Message Queues:** *Redis/RQ*, RabbitMQ, Celery, Kafka
- **Databases:** *MySQL/MariaDB*, PostgreSQL, SQLite, SphinxSearch

### Automation & Deployments

- **CI/CD:** *GitHub Actions*, Jenkins, CircleCI
- **Testing:** *Pytest*, *Testinfra*, Inspec, Docker
- **Version Control:** *Git*, SVN, Mercurial, Bazaar, CVS, RCS

### Infrastructure & Network Administration

- **DCIM/IPAM:** *Netbox*, Device42
- **Storage:** *LVM*, *Multipathd*, Ceph, NFS, NetApp, XIV, OCFS2
- **Common Protocols:** IPv4/IPv6, LACP, VRRP, *DNS*, *HTTP*, SMTP
- **Network Software:** *Unbound*, Bind9, HAProxy, Postfix, Dovecot
- **Network Hardware:** Unifi, pfSense, *OPNsense*, *Ferm*, Cisco iOS, Mikrotik
- **VPN:** OpenVPN, WireGuard, Tinc

### Security, Observability & Compliance

- **Directory Services:** Active Directory, RADIUS, LemonLDAP-NG
- **Security:** AppArmor, Fail2Ban, *Logcheck*, GPG, *McAfee Web Gateways*
- **Monitoring:** Grafana, ELK, Splunk, Zabbix, eHealth
- **Policies:** *HIPAA*, PCI-DSS, *CIS*, ITIL

## Professional Experience

### Utah Broadband, Phoenix, AZ

*Senior Systems Engineer* · Remote · October 2024 – Present

I joined Utah Broadband as the only Systems Engineer for AireBeam Fiber Internet, a sister company delivering high-speed fixed wireless internet to underserved residential areas. My position covered the breadth of system administration, network engineering, and security compliance needs that are common for Small and Medium Businesses (SMBs).

My primary responsibility was to support the Network Engineers, who were ultimately responsible for customer and employee support. This included reviewing RADIUS logs, deciphering MySQL schemas, and writing utilities to automate common networking tasks.

My secondary responsibility was to improve overall reliability and security posture, which included rebuilding servers with configuration management, replacing aging equipment, introducing usable security standards, and creating as much redundancy as possible within budget constraints.

The most exciting project during my tenure included a rare opportunity to deploy robust virtualization at a data center. This required reviewing existing resource usage, planning for growth, and balancing potential redundancy against financial budget. This also provided a unique opportunity to resolve many long-standing security issues that had been deferred due to technical debt and lack of resources.

After one year, the only three servers remaining to be migrated were blocked because they would create a customer-visible outage and required further network changes before proceeding.

**System Administration:**

- Deployed **Ansible** to adopt and manage all servers, enabling centralized configuration and audits
- **Rebuilt** many servers that were too old or fragile, making regular server updates possible
- Established a routine of regular software updates, providing windows of potential outages
- Created a company-wide **knowledge base** and populated with all known issues and standard processes
- Regularly reviewed **backup logs** and tested restoration, verifying quality of documentation
- Reviewed **server logs** every day, ensuring all anomalies were quickly addressed
- Separated **DNS** into public and private zones, removing private records from public view
- Wrote **health check** scripts that automatically repaired issues and notified administrators
- Automated **health checks** that self-recovered from known issues, reducing manual intervention
- Implemented **proactive monitoring** to alert on anomalies before they impacted service availability
- Created **runbooks** documenting common failure scenarios and automated recovery procedures

**Data Center Operations:**

- Rolled back an incomplete attempt to introduce a second data center, simplifying architecture
- Utilized **remote hands** to review existing hardware, removing unused servers and VPN devices
- Reviewed **capacity requirements** and made recommendations for new virtualization cluster
- Deployed and tested a 3-node **Proxmox** cluster, providing resiliency against potential failures
- Restructured **NetApp** storage, ensuring backup space will reach capacity before servers

**Security & Compliance:**

- Created a **security policy** for servers that balanced best practices against usability
- Wrote **automated tests** to ensure all configuration changes adhered to security standards
- Consolidated various "engineering" servers into a single device with strict **access controls**
- Enforced **user management**, revoking any account that was not documented and approved

**Network Administration:**

- Created an Ansible project for network engineers, encouraging normalized switch configurations
- **Trained** network engineers to effectively use Ansible in a git-based workflow
- Migrated switch backups to **version-controlled snapshots**, replacing a faulty backup process
- Maintained **RADIUS** services used for authenticating network devices and network engineers
- Configured **host-level firewall**, improving security that enabled a complete network rebuild

### Volkswagen Group of America, Auburn Hills, MI — via TEKsystems

*Linux Desktop Engineer (Project Contract)* · Remote · May 2022 – May 2024

I was contracted, through TEKsystems, to design and implement a Linux Endpoint for developers who were creating autonomous driving software at Volkswagen Group of America for brands including Volkswagen, Audi, Porsche, Bentley, Lamborghini, and Bugatti.

This project required identifying key stakeholders, gathering requirements, and designing a solution that improved the developer experience enough for them to embrace corporate security policies.

The final laptop image was fully-automated and secure. It supported self-service provisioning and recovery, secure boot with Nvidia GPUs, full-disk encryption with employee smartcards, and automated updates integrated with existing Change Control processes.

At the conclusion of this project, documentation and support were handed off to internal IT teams for ongoing support and maintenance. This included training sessions for support staff, documentation for end-users, escalation procedures for complex issues, and project documentation ready to present to the international Volkswagen Group.

**Business Analysis & ITIL:**

- Collected corporate **security policies** and **developer requirements** into a comprehensive project plan
- Collaborated with stakeholders to identify and document specific security exceptions for AI/ML teams
- Designed **layered authentication system** supporting regular employee access and privileged recovery
- Coordinated with Support Team Leads to provide support documentation, training, and escalation procedures
- Architected fully-automated **endpoint installer**, enabling both initial provisioning and remote rebuild
- Utilized staged provisioning process to provide **ready-to-use endpoints** for new hires and contractors
- Worked with Graphic Design team to create custom **branding** and **boot themes** for improved user experience
- Modified **boot-time messages** to provide clear instructions, reduce information overload, and guide recovery

**Software Development:**

- Created **self-service application**, letting end-users modify and repair their devices without IT assistance
- Customized **bootloader and login themes** to provide a comfortable and branded user experience
- Developed **boot-time recovery** system to repair common mistakes or even initiate full reinstallation
- Wrote **User documentation** guiding employees through Linux basics, team resources, and general AI engineering
- Delivered documentation using a **Static Website Generator**, ensuring fast and reliable access on every device
- Encouraged developers to contribute changes, giving some development teams their first **knowledge base**

**System Administration:**

- Engineered **Linux Endpoint** solution for 50+ AI developers that complied with corporate security policies
- Developed **automated installer** that built fully-configured and secure endpoints
- Enforced **secure boot** with Nvidia GPU support, enabling trusted execution of AI/ML workloads
- Integrated **automatic system updates** with existing Change Control processes, using test cycles for stability
- Extended **centralized logging** to include endpoints, improving troubleshooting and auditing capabilities
- Created **log alerts** to proactively notify users and support staff of potential issues

**Security & Compliance:**

- Implemented **full-disk encryption** using LUKS with PKI Smartcards and rotating backup keys
- Generated **unique rotating recovery keys** using device tokens, enabling support for lost smartcards
- Worked with system administration team to build an Active Directory proxy for user authentication
- Built **automated compliance tests**, ensuring every endpoint adhered to corporate security policies
- Automatically revoked **Device Posture Checks** when certain actions were performed, requiring config sync
- Integrated **antivirus** and **endpoint detection** software, working with Security Team to improve performance

### Basis Technologies, Chicago, IL

*Database Administrator / Site Reliability Engineer* · Remote · August 2021 – March 2022

I was hired as a Site Reliability Engineer on the Database Operations team to improve the reliability and performance of Big Data infrastructure supporting Advertising Technology. My team was responsible for maintaining high availability of MySQL and Hadoop clusters that processed millions of transactions per minute, requiring sub-millisecond response times and near-perfect uptime.

The primary goal for our team was maintaining critical servers and carefully testing changes that were requested by developers. This required a deep understanding of MySQL transactions, careful planning, and thorough testing to ensure that changes did not negatively impact overall database performance.

My most significant contribution came during a catastrophic incident where a database outage cascaded to backup servers, resulting in a complete stop to revenue generation.

I established an incident response process using active-research cycles, where one team member would babysit recovery while others investigated the root cause and developed a long-term repair plan. At each cycle, everyone would meet to discuss current findings, plan next steps, and hand off the active recovery effort to another team member.

Using this approach, we were able to maintain non-stop recovery efforts while simultaneously experimenting with alternative recovery methods. This allowed us to quickly pivot when a promising new method was discovered, and was ultimately responsible for reducing downtime from multiple days to under 12 hours, saving **over $800,000 per day** in lost revenue.

**Database Administration:**

- Supported **big data infrastructure** and daily operations, including MySQL clusters and Hadoop environments
- Created **documentation website** that replaced scattered notes, improving discoverability and overall quality
- Improved documentation based on external feedback, improving speed and quality of incident response
- Monitored **system performance** and resource utilization, with close attention to specific high-load queries
- Analyzed **database performance** metrics to ensure optimal settings were in place for production workloads

**Incident Response:**

- Detected early signs of **critical incidents** while on-call and maintained logs for **root cause analysis**
- Coordinated team efforts during high-severity incident, using active-research cycles to maintain momentum

**Server Administration:**

- Maintained **Linux servers** running MySQL and Hadoop, thoroughly testing all changes prior to deployment
- Reviewed system logs, performed regular updates, and ensured backups were successfully completed
- Automated **routine maintenance tasks**, reducing manual effort and eliminating common mistakes
- Reviewed incidents and logs to develop improved **monitoring checks**, reducing time to detection
- Wrote **documentation** to guide team members through common maintenance and troubleshooting tasks
- Created a **CI/CD pipeline** to automatically test configuration changes before deployment
- Utilized Pull Requests to create an informal **change control process**, improving cross-team communication

### Limelight Networks, Scottsdale, AZ

*Systems Engineer* · Remote · July 2020 – August 2021

I was brought into Limelight Networks, a Content Delivery Network (CDN) provider, to improve their configuration management system and assist with general system administration tasks.

After a series of organizational restructures, my primary responsibility was to ensure passwords were being regularly rotated for all service accounts. This required auditing existing scripts to find hard-coded passwords and monitoring system logs to identify currently-active versions of user names.

**System Administration:**

- Created Ubuntu 20.04 templates used for manual testing, beginning plans to migrate all servers
- Updated SaltStack configuration and scripts to support Python 3, enabling management of new servers
- Reviewed SaltStack customizations and provided patches to remove legacy bugs and improve stability
- Refactored a custom salt-bootstrap script to improve maintainability and reliability
- Reviewed system logs and configuration to identify and report all currently-active service accounts
- Regularly rotated passwords for all service accounts, ensuring compliance with security policies

### Taos Mountain, San Jose, CA

*Senior DevOps Engineer (Full-Time Employee / DevOps Consultant)* · Hybrid · July 2015 – June 2020

Consulting company that provided DevOps consulting services to a variety of clients.

Most of my time was spent augmenting internal IT teams with system automation and hardening expertise, as well as general Linux system administration support. During slower periods, I assisted with various internal company efforts.

**Internal Operations:**

- Conducted "Technical Interviews" of fellow consultants as part of regular career growth evaluations
- Wrote articles for company blog, focusing on safely applying strong security standards
- Read further for client-specific accomplishments [Juniper Networks, Suitable Technologies, Sony Pictures Entertainment]

#### Juniper Networks

*FTE Consultant via Taos Mountain* · Remote · October 2018 – June 2020

Juniper Networks was a multinational corporation that develops networking products.

I was brought into an established team of 22 Taos consultants to resolve bugs in a custom configuration management solution and improve the success rate of system hardening scripts.

My most impactful contribution required deep troubleshooting skills to identify the root cause of frequent remediation failures that were threatening to cut the project entirely.

Using a cloned VM and careful analysis of logs, I was able to identify several underlying issues that were causing the remediation process to fail. After writing patches to proactively resolve these issues, the **failure rate dropped from over 90% to only 1 failure** for the remainder of my tenure.

**Business Analysis:**

- Gathered requirements from internal IT staff to improve system hardening process
- Worked with multiple security teams to gain access to a VM that could reliably reproduce failures

**System Administration:**

- Followed manual package testing procedures to verify quality of custom configuration packages
- Wrote patches to resolve bugs in custom management solution, resolving over 90% of remediation failures
- Resolved performance issues in configuration scripts, eliminating over 80% of employee wait time
- Assisted with development of CI/CD pipeline to automatically test all changes and prevent regressions
- Continued supporting regular system administration tasks after the remaining Taos team was disbanded

**Software Development:**

- Wrote a script to search user directories for **insecure SSH keys**, ensuring compliance with security policies
- Updated key scanning script to support edge cases and **parallel execution**, enabling timely completion of scans

#### Suitable Technologies

*FTE Consultant via Taos Mountain* · Hybrid · July 2016 – August 2018

Suitable Technologies developed telepresence robots for business and personal use. I replaced another Taos consultant who was not meeting expectations because of my strong understanding of SaltStack and Linux internals, as well as a proven ability to work well with challenging clients.

I was primarily responsible for modernizing infrastructure, reducing security risks, and introducing redundancy to servers that drive customer-facing services.

My most significant series of contributions began when I was asked to review and refactor a custom user authentication mechanism for Jabberd2 that was preventing a **10-year-overdue upgrade**. After refactoring this patch, I built a custom Debian package to support multiple TLS versions, enabling seamless upgrade to a new service.

During that migration, serious performance problems were discovered with authentication, leading to the discovery of a critical 0-day vulnerability. Resolving this required closely reviewing the entire authentication stack and bringing a django token mechanism into the Jabberd2 plugin, enabling an effective cache solution. This completely resolved the performance issue that led to the insecure configuration. This cache was later made redundant by extending a python dictionary to Redis.

**System Administration:**

- Resolved performance issues in SaltStack configuration, reducing execution time from **hours to minutes**
- Refactored management of secret keys, preventing information leakage and improving server scalability
- Constructed new backup solution based on least-access principles, removing use of root SSH keys
- Modified deployment process to enable rotation of initial root passwords, improving security posture
- Wrote scripts to automate regular system administration tasks, reducing manual effort and errors

**Security & Compliance:**

- Discovered and resolved a critical 0-day vulnerability that allowed bypass of user authentication
- Reviewed system configuration to identify and resolve security vulnerabilities

**Software Development:**

- Refactored a custom authentication patch for Jabberd2, enabling a 10-year-overdue upgrade
- Built multi-binary Debian package for Jabberd2, enabling TLS 1.2 support and seamless upgrade
- Designed and implemented an **in-memory cache** to improve authentication performance, preventing DoS
- Replaced in-memory cache with **Redis**-backed solution, providing redundancy and improved performance

#### Sony Pictures Entertainment

*FTE Consultant via Taos Mountain* · On-Site · July 2015 – June 2016

Sony Pictures Entertainment is a multinational media and entertainment corporation.

Although I was part of a larger team of Taos consultants focused on a larger cleanup effort, my primary responsibility was to assist with system hardening and automation for an air-gapped subsidiary network.

My most significant contribution was reviewing CIS Level 2 benchmarks for Linux servers and creating automated solutions to enforce selected policies. This included writing Chef recipes to apply selected recommendations, as well as testing and validating each change to ensure no negative impact to production servers.

**System Administration:**

- Supported standard system administration activities including patching, updates, and issue resolution
- Deployed and maintained **RHEL Satellite** server for repository mirroring and client license management
- Automated **Satellite** deployment and configuration, ensuring server could be regularly rebuilt
- Developed comprehensive **Chef recipes** to enforce security recommendations across production servers
- Thoroughly **tested** and validated policy changes to ensure zero negative impact to production workloads

**Security & Compliance:**

- Reviewed **CIS Level 2** benchmarks for Linux servers and implemented every possible recommendation
- Documented every **policy** change, providing clear justification for any deviations from CIS recommendations

### Good Samaritan Society, Sioux Falls, SD

*Senior Systems Administrator (SRE)* · On-Site · February 2011 – March 2016

I was the only Linux Administrator in the nation's largest not-for-profit long-term healthcare provider, supporting over 10,007 employees across more than 300 remote Skilled Nursing Facilities with many more branch facilities.

My primary responsibility was maintaining all Linux servers, including application servers, print servers, file servers, and remote "boothost" servers, as well as most applications running on these servers.

My most impactful contributions were focused on supporting employees at remote facilities, where I developed a deep understanding of unique challenges faced by the nursing staff who were directly caring for patients. These challenges were often accepted as "just the way things are" because of the high-stress environment and limited response from historical complaints, giving me nearly unlimited opportunities to create meaningful improvements.

I was extremely fortunate to work in an environment that encouraged deep learning and creative problem solving, giving me the time and freedom to make sure that every problem ticket remained open until a true solution was found.

**System Administration:**

- Introduced to environment by a database server that was days from complete failure
- Managed server software and hardware for more than 500 Linux servers
- Assisted with management and troubleshooting of over 200 Windows and 50 AIX servers
- Automated server deployment and rebuilt all servers, providing fully configured remote servers
- Provided life support for over 150 remote servers running in harsh conditions (smoke, flood, etc.)
- Created a fully automated ESXi deployment system with auto-deployed and encrypted guests
- Connected remote servers to monitoring system, gaining insight into previously-unknown failures
- Prepared and shipped replacement servers, allowing planned outages that saved $400 per incident
- Introduced **configuration management**, enabling roll-out of standardized configuration
- Maintained centralized **print server** used to send special reports to remote line-feed printers
- Optimized scripts for efficiency, improving execution time from days (or weeks) to hours.
- Provided critical support during many migrations, including MS AD, Exchange, XIV, hardware refresh, etc.
- Worked closely with network team to resolve countless network issues impacting remote facilities

**Incident Response:**

- Took over for a coworker when a Netware failure took down the company file server, focusing on recovery
- Gathered enough data to identify critical teams and bring together for a coordinated recovery effort

**Security & Compliance:**

- Managed McAfee Web Gateways and Web Reporter that were responsible for internet security
- Utilized Active Directory deployment to automate certificate trust, enabling Data Loss Protection
- Replaced network authentication with NTLMv2, completely eliminating additional manual logins

**Support & ITIL:**

- Supported remote "boothost" servers that were used to facilitate employee access to corporate network
- Gained enough knowledge to provide basic support for all applications used at every remote facility
- Provided an extra tier of support for other teams, ensuring all employee-faced issues were solved
- Wrote documentation to guide support staff through recurring issues, improving first-call resolution
- Established regular meetings with call center managers, completely eliminating some common problems

**Software Development:**

- Created a custom DCIM/IPAM website, replacing a slow document-based change request process
- Wrote scripts to scrape and parse legacy MS Office documents to extract network device information
- Developed a self-service file-restore application that eliminated hours of manual effort
- Wrote patches to resolve security-related issues in financial and healthcare applications

**Database Management:**

- Deployed and maintained a 5-node multi-master MySQL/MariaDB Galera cluster, replacing fragile instance
- Planned database servers to reduce split-brain potential, ensuring network hiccups never cause an outage
- Monitored database performance and worked with development teams to optimize queries
- Worked with database engineer to refine complex queries needed to extract data from a large database

### Kalliki Software, Sioux Falls, SD

*System Administrator / Website Developer* · On-Site · July 2009 – December 2010

Ten-person website development start-up company building websites with customer needs ranging from personalized themes to complex document sharing platforms.

I was responsible for all server administration tasks that supported a small development team and kept customer websites online.

**Website Development:**

- Migrated websites from Wordpress, Joomla, and custom code to Drupal, often removing hidden defacement
- Created custom Drupal modules to address unique customer requirements
- Controlled access to staging websites, offering customer sign-off prior to delivery
- Integrated client approvals with billing platform (Quickbooks), completely eliminating unpaid bills
- Trained other website developers, with a focus on troubleshooting PHP websites
- Worked closely with graphic designer and external vendor to ensure every custom website theme was possible

**Business Analysis:**

- Attended customer meetings involving custom module development, enabling immediately-accepted quotes
- Provided clean transition when company was sold to a competitor that was transparent to customers

**Business Development:**

- Absorbed graphic design team into development team, improving product quality and employee satisfaction
- Interviewed prospective employees using sprint-style tasks designed to focus on feedback-driven development
- Set up and managed Mailman mailing lists that were used for internal and external communication

**System Administration:**

- Designed and implemented a secure, scalable Nginx+PHP stack, hosting over 50 isolated client websites
- Monitored system logs and resource usage to automatically notify administrators of potential issues
- Daily review of system logs to ensure no users have logged into production servers
- Wrote CI/CD pipelines that automatically tested and deployed server configuration changes and OS updates
- Designed, implemented, and validated disaster recovery procedures
- Regularly updated all servers and workstations

**Network Administration:**

- Coordinated with building network engineers, maintaining zone for secure internal development

### Secure Banking Solutions, Madison, SD

*Application Developer* · On-Site · April 2007 – February 2008

Consulting services for banks, with a focus on **risk assessments** and **penetration tests.**

**Software Development:**

- Wrote script to automate generation of penetration test reports, eliminating over 40 hours of effort per report
- Assisted with development of Technology Risk Assessment Calculator (TRAC) utility, used to complete audits
- Developed the first web-based version of TRAC, eliminating many customer-visible performance issues
- Created USB-based phishing utility that enabled auditors to safely identify users needing additional training
- Wrote mailing list plugin for company website that yielded a 20% increase in customer response rate

**System Administration:**

- Introduced virtualization in order to provide virtual workspaces to pen testers using spare resources
- Rebuilt BackTrack servers with Debian, removing many well-known internal security concerns
- Performed regular OS and software updates to ensure latest security patches were applied

## Education

### Dakota State University, Madison, SD

*Bachelor of Science* in **Business and Computer Information Systems** · September 2006 – December 2010

**Minors:**

- Network Security
- Networking

**Specialization:** Systems Development

## Certifications

My primary drive for pursuing certifications is to meet employment and volunteer requirements. In my free time, I prefer to focus on learning new skills and technologies through hands-on experience.

| Certification | Dates | Record ID |
|---|---|---|
| **SSCE** (SaltStack Certified Engineer) | Mar 2015 | [71C6EC7](https://ssc.saltstack.com/) |
| **GCP - Professional Cloud Architect** (Google Cloud Platform) | Apr 2019 – Apr 2021 | [xu2dH](https://www.credential.net/k315bwjm) |
| **CITI - Cancer GCP** (Good Clinical Practice) | Feb 2019 – Dec 2024 | [46415](https://www.citiprogram.org/verify/?w14434623-225d-451c-9b98-1d8894ae6658-46415) |
| **CITI - Investigators HSR** (Investigator Health Science Research) | Feb 2019 – Dec 2024 | [46416](https://www.citiprogram.org/verify/?w61a429ad-2988-48e1-a11f-1d0b43737520-46416) |
| **CITI - IRB HSR** (Institutional Review Board HSR) | Feb 2019 – Dec 2024 | [46414](https://www.citiprogram.org/verify/?w2f7881f1-dca7-4bfb-91ff-816694cbff43-46414) |
| **CITI - Cancer HSR** (Cancer Health Science Research) | Feb 2019 – Dec 2024 | [46417](https://www.citiprogram.org/verify/?w263ac87a-5df9-4ab9-b326-19622be3d875-46417) |

## Home Laboratory

Further details and a *Network Diagram* are available at [https://personal-url.tld/homelab](https://personal-url.tld/homelab)

My home lab was born **from a need to test major changes** in a workplace where no test environment was currently possible. This lab was treated like an enterprise environment and grew into a full-scale, hybrid (multi-cloud) deployment with redundant services that were used by various open source projects.

- Began as **pfSense** and **Proxmox**, to test upgrading remote hardware from **Debian** 4 to 6
- Utilized **VLANs** and **Subnets** to replicate multiple remote facilities connected to Central Office
- Throttled bandwidth to **replicate real-world lag** introduced by T1 network connections
- Added Cisco switch (iOS) to learn about **Link Aggregation (LAGG)** and investigate workplace challenges
- Migrated to Mikrotik switches and added hardware to support **fully-redundant stack**, with failover ISP
- Created **Out-of-Band** management device using cellular modem to guarantee remote access
- Introduced **IPv6** to specific VLANs, enabling access to certain websites prior to ISP support for IPv6
- Secured access to VLANs using **bastion hosts** that required "ssh key + password + 2FA"
- Experimented with all available **Configuration Management** solutions, including home-grown scripts
- Implemented every **security standard** that could be found, evaluating for efficacy and usability
- Introduced all changes (and deployments) using **SaltStack** after **CI/CD** (automatic tests) passed
- Wrote thousands of **unit and integration tests** to provide the best chance of a successful update
- Re-deployed infrastructure from scratch, ensuring entire stack (**metal to cloud**) can be automatically rebuilt
- Expanded infrastructure to **cloud** platforms, using **VLANs** and **VPN** to maintain tight security
- Utilized Netbox for **DCIM/IPAM** (Data Center Inventory Management / IP Address Management)
- Updated the environment via **git** and **netbox**, with **Salt** responsible for actual modification
- Backed up data to **AWS Glacier** using **GPG** for fully-encrypted backups and **squashfs** for space efficiency
- Managed personal and family devices using **automation stack**, gaining a second opinion on **usability**

## Presentations

### From Server Chaos to Order with SaltStack, SaltConf15

2015

Presented my experience using SaltStack to bring order to a chaotic server environment. This included lessons learned, best practices, and practical advice for others attempting similar projects.

## Volunteer Experience

Some of my most meaningful contributions have come from volunteer work:

### Tallgrass Recovery

September 2020 – November 2024

Non-profit organization that provides support and resources for individuals recovering from substance abuse and addiction. Focus on community outreach, education, and advocacy.

- Mentored individuals in recovery, walking them through the early steps of sobriety
- Presented my personal story, helping others understand the line between bad habits and addiction

### Avera Oncology Institutional Review Board

February 2019 – April 2023

Avera Oncology is a regional cancer treatment center that serves patients across multiple states. The Institutional Review Board (IRB) is responsible for reviewing clinical research studies to ensure patient safety and regulatory compliance.

- Served as non-scientific/unaffiliated patient-representative
- Also served on Health Science IRB (February 2021 – April 2023)
- Reviewed studies to ensure human subjects were properly protected (Belmont Report)
- Became familiar with industry standards and regulations (FDA, OHRP, HIPAA, etc.)
- Reviewed patient consent forms for completeness, accuracy, and clarity

### Upper Midwest Great Dane Rescue

March 2012 – November 2023

Non-profit organization that rescues, rehabilitates, and rehomes Great Danes in need. Focus on education, responsible pet ownership, and breed-specific health issues.

- Transported Great Danes hundreds of miles with frequent comfort stops, delivering them to new homes
- Conducted home visits to ensure prospective adopters provided a safe and loving environment
- Visited animals in shelters to provide socialization, exercise, and basic training

### Kids Against Hunger

February 2012 – September 2013

Non-profit organization that packages and ships nutrition-packed dry meals to struggling communities both locally and internationally, with a focus on teaching children to enjoy helping others.

- Assisted with packaging dry food for international shipment
- Led volunteer pack sessions of 10-80 volunteers, coordinating teams rotating kids through stations
- Unloaded bulk shipments and prepared tables for packing events, ensuring smooth workflow
- Presented training session prior to each event, ensuring all volunteers understood who they were helping
- Assisted more experienced pack leaders with larger events, often taking over for frustrated parents

## Open Source Contributions

Well-known open source projects I have contributed to over the years include:

### Debian Linux

December 2009 – Present

Debian is a widely-used Linux distribution known for its stability, security, and extensive software repository. I was granted Debian Developer status in 2015 after years of maintaining packages, reviewing contributions, triaging bugs, assisting new developers, and participating in various teams.

- Obtained '**Debian Developer, with uploading rights**' status in 2015, gaining unrestricted upload access
- Maintained packages in Debian repositories (nginx, tdc, etc.), ensuring **safe updates for millions of servers**
- Joined "ftpteam", reviewing packages to ensure **open source standards** are maintained
- Reviewed and sponsored packages on behalf of prospective Debian Developers
- Triaged and resolved bugs reported in **bug tracking system**, using bug tracker as a customer support tool
- Uploaded packages to **Debian build system**, including backports, and coordinated security updates
- Verified OpenGPG identities for inclusion in the Debian Keyring, ensuring a strong **web of trust**

### Ubuntu Linux

October 2005 – February 2019

Ubuntu is a popular Linux distribution based on Debian, known for its user-friendliness and regular release cycle. I was voted into the Ubuntu Community Membership team in 2009 because of my consistent contributions to user support, local community groups, Ubuntu News content, and development of tools for community projects.

- Obtained '**Ubuntu Member**' status in 2009
- Supported users through **IRC support channels** and mailing lists, providing peer-based learning
- Assisted in development of infrastructure for **Local Community teams**, improving community outreach
- Worked with Canonical to develop new **branding guidelines**, creating consistency across community projects
- Developed tools for community projects, including **Drupal modules** that were used by the official website
- Contributed **content and reviews** for the Ubuntu News and Website teams

### SaltStack

August 2011 – January 2024

SaltStack is an open-source configuration management and orchestration tool used to automate the deployment and management of IT infrastructure. I was an early adopter and became a contributor to the project so that my improvements could be reviewed by peers and included in future releases.

- Provided support via IRC channels, mailing lists, and GitHub issues
- Worked with developers to resolve security and performance issues
- Refactored Debian networking modules and templates
- Wrote first version of the "debconf" execution/state modules
- Provided patches to fix issues with Proxmox, documentation, etc.

### Nginx Web Server

February 2009 – May 2023

Nginx is a high-performance web server and reverse proxy server known for its speed, scalability, and low resource consumption. I contributed to the Nginx community by maintaining Debian packages, managing community resources, and providing support to users.

- Built, packaged, and distributed the Nginx web server packages for Debian
- Deployed and managed servers and software for the Nginx Wiki and Planet
- Built community projects, support system, and documentation repository
- Served as Group Contact for all Nginx IRC channels on Freenode
- Provided features/patches now included in Nginx source
- Served as a community point of contact

### Gitea

October 2016 – December 2018

Gitea is a lightweight, self-hosted Git service platform that provides a simple and efficient way to manage Git repositories. I spent hundreds of hours cleaning up the code base and providing patches to ensure all external libraries were documented and properly licensed.

- Reviewed all golang and javascript libraries used in the project and organized into vendor directories
- Verified licenses for all external libraries, ensuring compliance with open source standards
- Authored more than 200 packages in the Debian repository to support Gitea in the main archive
- Created and maintained Debian packaging for Gitea, ensuring safe and reliable installation for users
- Provided patches to resolve various bugs and issues reported by users
