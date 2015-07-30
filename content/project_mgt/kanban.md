---
title: Kanban Practices
summary: Kanban in the context of software development mean a visual process-management system that tells what to produce, when to produce it, and how much to produce - inspired by the Toyota Production System and by Lean manufacturing.

---

Kanban in the context of software development mean a visual process-management system that tells what to produce, when to produce it, and how much to produce - inspired by the Toyota Production System and by Lean manufacturing.

A Kanban board must be visual, tactile, collaborative.  

## Kanban Composants 

The Kanban composants are :

* Kanban cards representing pieces of work. The cards can support various information as :
    * assignee
    * start time
    * end time
    * type of task (eg. bug vs feature vs tech debt (usually code enhancements))
* Labeled containers for the cards representing the different stages of a workflow, the life-cycle of a task/story
* Constraints
    * information on the exact product or component specifications that are needed for the subsequent process step, ie. to pull task/story from column to column
    * max number of cards a column can contain

Examples:
A minimal Kanban board is a board with columns "To Do", "Doing", "Done":

![](http://leankit.com/kanban/what-is-kanban/kanban-board-e60650d1.jpg)

The most popular example of kanban board for agile or lean software development consists of: Backlog, Ready, Coding, Testing, Approval and Done columns. It is also a common practice to name columns in a different way, for example: Next, In Development, Done, Customer Acceptance, Live.

![](http://i1.wp.com/www.everydaykanban.com/wp-content/uploads/2012/03/kanban-board.png)


## Core Kanban Principles

* Visualize the workflow, showing the work in progress, the work remaining and showing the flow of work through the Kanban system
* Limit the Work in Progress (WiP), and then reduce the time it takes an item to travel through the Kanban system
* Manage the Flow
    * Visualize blocked items, long queues, empty spaces
    * Deal with indicators of problems
    * Analyze the flow with metrics
* Implement Feedback Loops
* Make Process Policies Explicit
* Improve Collaboratively

The Kanban method starts with existing roles and process and stimulates continuous, incremental and evolutionary change in the system by monitoring, adapting and improving the workflow, by measuring effectiveness by tracking flow, quality, throughput, lead times.


## Kanban Metrics

First some definitions to understand Kanban Metrics.  
Lead Time : The time it takes a work to get from step A to step B.  
![](http://leankit.com/kanban/lean-flow-metrics/images/Lead-Time-4d568f72.png)
There can be several lead times (e.g., customer lead time, development lead time, QA lead time, etc.) and specially the End to end Lead Time : The time in which a card goes from being created to being closed.

Delivery/Cycle Lead Time : The time a card spend out of the backlog, ie. the elapsed time from the moment someone start working on a story until it is done.
![](http://leankit.com/kanban/lean-flow-metrics/images/Cycle-Time-e537190e.png)
Different teams will use different definitions for start and done ("accepted by the product owner" vs "delivered to production").


### Cumulative Flow Diagrams
This report represents the relative amount of work for each stage of project over the time.
The key data points of the CFD are:

* The vertical distance between each area represents the amount of work in progress on the respective stage in a specific date
* The horizontal distance between the areas in the chart corresponds to the average lead time of the requests that arrived on a specific date
* The mean delivery rate, represented by the slope of the closed items area, corresponds to the trend in the delivery of the work (the triangle in the chart provides a visual representation of "Little's Law")

This metric help understand the state of current work  and what might need to be done to speed up the pace of delivery.  
The diagram should run smoothly. Large steps and flat horizontal lines indicate impediments to flow or lack of flow. Variations in the gap or bands stand for bottleneck situations, which usually occur due to irrelevant work in progress limits.
![](http://static.kanbantool.com/seo-landing-page/kanban-presentation/cumulative-flow-chart7.png)
![](http://static.kanbantool.com/seo-landing-page/kanban-analytics-and-metrics/lead-cycle-time-diagram-kanban-tool-10.jpg)


### Lead Time Average

This report shows a trend of the average number of days a task took to be completed, from start to finish. It is categorized by work item type so teams can see the how the system is performing over time, broken down by work item type. 

### Flow Efficiency 

This report shows the average percentage of lead time that a developer spent working on a task (touch time). This shows the potential for process improvements. 


![](https://jazz.net/library/content/articles/insight/1.1.1.1/kanban-metrics/images/3.jpg)

### Cycle time diagram
Stacked bar chart representing how much time a task has spent in a given state through is life-cycle, allowing the detection of tasks that are taking too long.
![](http://blog.kanbanize.com/wp-content/uploads/2014/01/cycle-time-no-done-column.png)

### Due Date Performance 

This report shows the percentage of items that were delivered on time and the average percentage delivery rate over time. This is useful for illustrating how predictable the system is. Due date performance with a low percentage provides evidence that there is an abundance of variability in the flow. The team should take corrective action or they will not be able to establish reasonable service agreements. 

 
### Bugs per Story 

This report shows a trend of the average number of defects opened against a Story. Attaining predictability is a fundamental aspect in the Kanban system, however, that will be ineffective if the software is delivered with low quality. This chart is also useful when implementing Kanban to help teams establish goals in the quality area. 

### Lead Time Distribution 

  This report is a statistical distribution that shows the number of occurrences by lead time. It is an effective way to identify discrepancies in the process and boosts the confidence of teams in the definition of service level agreements, based on real life data. 

### Throughput Trend 

   This report shows the number of items that were delivered in a given time period (eg monthly). It can be used to identify a trend of how well the system has been performing. As teams work on process improvements, the throughput trend will show a more consistent slope in the chart. 

![](https://jazz.net/library/content/articles/insight/1.1.1.1/kanban-metrics/images/4.jpg)


<!--
##Kanban Strategies:
a kanban by project?
a kanban by team? a kanban by team seems more as one of the goal is to improve collaborative work.  
Team kanban can be combined with techniques like user map stories which allow to visualize project big pictures. 
-->

## Building a kanban

Methodologies to validate the model:

* Produce a sketch from your top-down or bottom-up model.
* Make sure that actual work items map to your sketch or top-down model, then use the "what does this item need?" questions.
* Consider whether it would be helpful to group, consolidate, or break down categories.


Links:

* Explain Kanban practices with a game [Kanban Pizza Game](http://www.agile42.com/en/training/kanban-pizza-game/)
* Kanban Board App [Trello](http://trello.com)
* Kanban Board App [Restyaboard](http://restya.com/board/)

### Six Rules for an Effective Kanban System

To ensure a proper setup of Kanban in the workplace, Toyota has provided us with six rules for an effective Kanban system:  
Customer (downstream) processes withdraw items in the precise amounts specified by the Kanban.  
Supplier (upstream) produces items in the precise amounts and sequences specified by the Kanban.  
No items are made or moved without a Kanban.  
A Kanban should accompany each item, every time.  
Defects and incorrect amounts are never sent to the next downstream process.  
The number of Kanbans is reduced carefully to lower inventories and to reveal problems.  

Sources:

[Kanban from the Inside: 20. Model workflow](http://positiveincline.com/index.php/2015/06/kanban-from-the-inside-20-model-workflow/)  
[Kanban Story](http://blog.crisp.se/2009/06/26/henrikkniberg/1246053060000)  
[Kanban Metrics: Measure Cycle Time To Stay Lean](http://blog.assembla.com/AssemblaBlog/tabid/12618/bid/102123/Kanban-Metrics-Measure-Cycle-Time-To-Stay-Lean.aspx)  
[7 LEAN METRICS TO IMPROVE FLOW](http://leankit.com/kanban/lean-flow-metrics/)  
[Improve predictability and efficiency with Kanban metrics using IBM Rational Insight](https://jazz.net/library/article/1350)  
[A brief introduction to kanban](https://www.atlassian.com/agile/kanban)
