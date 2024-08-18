
# Postmortem Report: API Gateway Outage

## Issue Summary

- **Duration**: August 10, 2024, 14:15 - 16:30 UTC (2 hours 15 minutes)
- **Impact**: During the outage, our API gateway experienced significant downtime, leading to the disruption of all API requests for approximately 75% of our users. This affected the ability of users to access essential services such as user authentication, payment processing, and data retrieval.
- **Root Cause**: The root cause of the outage was a misconfigured Nginx server update that inadvertently removed critical load-balancing rules, causing requests to fail to reach backend services.

![System Architecture Diagram](postmorterm_technical.webp)

## Timeline

- **14:15**: The issue was detected by our monitoring system, which triggered a high number of failed requests and increased latency alerts.
  
![Monitoring Dashboard Screenshot](https://grafana.com/static/img/docs/grafana/latest/visualizations/graph-panel/graph-panel.png)

- **14:18**: On-call engineer received an alert and began investigating the API gateway logs to identify the root cause.
- **14:25**: The engineer initially assumed a potential network outage and began testing network connectivity between the API gateway and backend services.
- **14:35**: After ruling out network issues, the engineer reviewed recent deployment logs and identified a Nginx configuration update as the potential culprit.
- **14:45**: The issue was escalated to the DevOps team to verify the Nginx configuration and identify any misconfigurations.
- **15:05**: The DevOps team identified that the load-balancing rules were missing from the Nginx configuration file after the recent update.

![Nginx Configuration Snippet](https://www.nginx.com/wp-content/uploads/2017/04/NGINX_Server_Block.png)

- **15:20**: A temporary rollback of the Nginx configuration was initiated to restore service, but it failed due to missing backups of the previous configuration.
- **15:45**: The team manually restored the correct load-balancing rules and restarted the Nginx service.
- **16:00**: API services began recovering, with normal operations fully restored by 16:30 UTC.
- **16:45**: A post-recovery analysis was conducted to ensure no further issues were present.

![Timeline of Events](https://www.mockplus.com/web/2022/02/25/6218607ddad65e7c1a3d8c65.jpg)

## Root Cause and Resolution

The outage was caused by a misconfiguration during a routine update of the Nginx server on the API gateway. The update script was supposed to include load-balancing rules to distribute traffic across multiple backend services, but an error in the script resulted in these rules being removed. Consequently, incoming API requests could not be routed correctly, leading to widespread service disruptions.

To resolve the issue, the team identified the missing configuration and manually restored the load-balancing rules. The Nginx service was then restarted, which gradually restored the API gateway's functionality.

## Corrective and Preventative Measures

**Improvements:**

- Enhanced deployment scripts to include automated configuration checks.
- Strengthened backup protocols to ensure that previous configurations are stored before any updates.
- Improved monitoring to detect configuration changes that could impact service availability.

**Tasks:**

1. **Patch Nginx server**: Update deployment scripts to include automated validation of critical configuration elements.
2. **Add monitoring on configuration files**: Implement a monitoring tool to detect and alert on unauthorized or unexpected changes to key configuration files.
3. **Establish backup protocols**: Ensure that a backup of the configuration is automatically created before any updates are applied.
4. **Conduct team training**: Provide training for engineers on the importance of configuration management and the potential impacts of misconfigurations.
5. **Review and test rollback procedures**: Regularly test rollback procedures to ensure they can be executed quickly and effectively in the event of an outage.

![Flowchart of Incident Response](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*HsDazmT2HXNHDuU23hRt-w.png)

This postmortem highlights the critical need for stringent configuration management and robust monitoring to prevent future outages and ensure the stability of our services.
