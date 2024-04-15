0x19-postmortem


Issue summary:
Users report inability to connect to the remote server which continued for 2 hours along.From 1:30 PM to 3:30 PM (GMT+2)
Most user requests resulted in 500 errors at peak 100% the team reached to the route cause which was the misconfiguration of the router .


Timeline:

At 1:30 PM  Incident Onset: Users report inability to access the application.
At 1:45 PM Initial Diagnosis: The operations team notices high CPU and memory usage on the database server.
At 2:15 PM Isolation: Load balancer logs indicate a spike in database queries before the outage.
At 2:30 PM the team reached the cause that made the server works poorly.
At 3:30 PM the team has solved the problem and the server starts to function properly.mm




Root cause and resolution :
Root Cause Analysis: Investigation reveals a recent code deployment introduced a poorly optimized database query.
Resolution: Temporarily rolled back the deployment and optimized the query to reduce database load.
Preventive Measures: Implemented stricter code review process for database queries and enhanced monitoring for database performance metrics.


Corrective and preventative measures:

Thoroughly test code changes before deployment.
Monitor system metrics proactively to catch performance issues early.
Implement automated alerts for abnormal database behavior.


