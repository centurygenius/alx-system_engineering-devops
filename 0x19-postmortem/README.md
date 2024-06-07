Postmortem Report: Service Outage Case Study

Incident Overview

Date and Time:     March 15, 2024, 10:00 AM - 1:00 PM WAT
Duration:          3 hours
Service Affected:  Online Music Streaming Web Application
Impact:            Users were unable to stream music, access playlists, or perform searches.

Issue Summary:

On March 15, 2024, our online music streaming service experienced a significant outage that lasted for three hours. This commenced from 10:00am to 1:00pm WAT. 
						
![service_outage_1](https://github.com/centurygenius/alx-system_engineering-devops/assets/136092053/9955408c-bc33-4cda-a82e-de42382a246a)

This disruption prevented all users from streaming music, accessing their playlists, and performing searches. The root cause was traced to a database connectivity issue exacerbated by a recent update to the database driver.

Timeline:

o	09:45 AM WAT: Deployment of the new database driver update.
o	10:00 AM WAT: First alerts received about database connection failures.
o	10:15 AM WAT: Incident response team engaged.
o	10:30 AM WAT: Initial investigation pointed to the database driver update.
o	11:00 AM WAT: Rollback of the database driver update initiated.

				![time_line_image_2](https://github.com/centurygenius/alx-system_engineering-devops/assets/136092053/d35c9fe8-84f5-48cd-9209-cf601942ab3f)

o	11:30 AM WAT: Rollback completed, but connectivity issues persisted.
o	12:00 PM WAT: Deep dive into the database configuration and network settings.
o	12:30 PM WAT: Identified and fixed misconfigured network security settings.
o	01:00 PM UTC: Full restoration of service confirmed.


Root Cause:

The primary cause of the outage was a bug in the newly deployed database driver, which was incompatible with our current database configuration. 
![service_root_cause_3](https://github.com/centurygenius/alx-system_engineering-devops/assets/136092053/d2ce78d1-c674-4727-92c8-54ec5a20f916)

					
This led to persistent connectivity issues that were further compounded by a misconfiguration in the network security settings.


Corrective and Preventive Measures:

o	Testing: Implement more comprehensive pre-deployment testing for database driver updates, 
	including stress tests and compatibility checks.

o	Redundancy: Improve redundancy in database configurations to ensure that single points of failure do not lead to service outages.

						
![service_correction_4](https://github.com/centurygenius/alx-system_engineering-devops/assets/136092053/4fd74ca3-e29d-4b61-ba80-78eb190e2f69)

o	Incident Response Training: Conduct regular training for the incident response team to handle similar issues more efficiently.

o	Documentation: Update internal documentation to include specific troubleshooting steps for database connectivity issues.

