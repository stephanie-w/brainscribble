---
title: Cumulative Flow Diagram
status: draft

---


<!-- BEGIN_SUMMARY -->
The Cumulative Flow Diagram report represents the relative amount of work for each stage of project over the time.
<!-- END_SUMMARY -->

The key data points of the CFD are:

* The vertical distance between each area represents the amount of work in progress on the respective stage in a specific date
* The horizontal distance between the areas in the chart corresponds to the average lead time of the requests that arrived on a specific date
* The mean delivery rate, represented by the slope of the closed items area, corresponds to the trend in the delivery of the work.



Little's law says the long-term average number of customers in a stable system $L$ is equal to the long-term average effective arrival rate, $\gamma$, multiplied by the (Palm‑)average time a customer spends in the system, $W$, or expressed algebraically: 
$L = $\gammaW$  
If you have the mean number n a system and the throughput, the Little's Law gives the average response time like so:  
$MeanResponseTime = MeanNumberInSystem / MeanThroughput$

In a Kanban system, using the Project Terminology, we have:
$LeadTime = WIP / Throughput$ where
$WIP$ = average number of items in process = $L$
$Throughput$ = average departure rate = $\gamma$, .ie average number of work items (exiting) the workflow per some unit time
$LeadTime$ = average time an item spends in the system = $W$, .ie the average time it takes a work item to move through the workflow from start to delivery 

<!--
The power of Little’s Law to Kanban teams is not its ability to predict WIP, Thoughput or Leadtime. The true power lies in its ability to influence team behavior with its underlying assumptions. 

In other words, if you want to:
* increase Throughput then limit WIP
* speed up the process, i.e. reduce Lead Time, then once again limit the WIP
-->



![](https://jazz.net/library/content/articles/insight/1.1.1.1/kanban-metrics/images/2.jpg)
![](http://static.kanbantool.com/seo-landing-page/kanban-presentation/cumulative-flow-chart7.png)
![](http://static.kanbantool.com/seo-landing-page/kanban-analytics-and-metrics/lead-cycle-time-diagram-kanban-tool-10.jpg)
-->
