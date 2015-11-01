---
title: Kanban Principles
date: 2015-07-02

[TOC]

---

<!-- BEGIN_SUMMARY -->
Kanban in the context of software development mean a visual process-management system that tells what to produce, when to produce it, and how much to produce - inspired by the Toyota Production System and by Lean manufacturing.

<!-- END_SUMMARY -->
Kanban board core properties are:

* visualize the work in the worflow
* limit the work in progress
* manage flow
* make process policies explicit
* improve collaboratively

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

![](figure/kanban-board-1.png)

The most popular example of kanban board for agile or lean software development consists of: Backlog, Ready, Coding, Testing, Approval and Done columns. It is also a common practice to name columns in a different way, for example: Next, In Development, Done, Customer Acceptance, Live.

An other common one is:

![](figure/kanban-board-2.png)

Possible workflow step could be chosen among the following steps:

* Backlog
* Ready/Selected
* Coding/Development
* Testing
* Acceptance/Approval
* Deployment
* Done/Live

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

## Building a kanban

** A methodology to discover WIP**  
On a sheet of paper, ask the team to write down 5-10 things you're currently working on.  
For each items, the team should answer the following questions:

* what type of work is it? (user story, feature, defect, task, request, ticket, white pater, test, etc.)
* where is it now? (in development, waiting for, etc.)
* where was it just before I got it?
* where will it go when i'm done with it? (ready to deploy, in production, etc.)

The resulting material is the base for a first shot of the mapping of the workflow, drawing a board representing the path from a task entering the system (ie. the team sharing the same process) to the done step, trying to find a place for each piece of work.  
First, examine the entering work by identifying the source of demand: What's the cause of event? What is the source of demand? Then what is the destination of the completed work?: software development environment, test platform, etc.?   
The next step is identifying the queues, places where tasks are waiting to be picked by someone and to be moved to the next step (ex: a "development done"or a "Ready to deploy" column). A important point is also to identify who owns the queues (the development team, the QA team,...) cause the limit WIP should be base on the process limit of the owner.  
A Kanban is a "pull" system, the work is pull along by the owner of the queue when it is ready for it and has the capacity to work on it. This helps balancing the demand against the available throughput preventing bottleneck.

Even if the mapping will be reajusted, improved from time to time, it is important to track work progess by collecting metric starting with basic Kanban metrics: Total WIP, #Blockers, Troughput (Cards complete/day or week).

## Kanban Metrics

First some definitions to understand Kanban Metrics.  
Lead Time : The time it takes a work to get from step A to step B.  

![](figure/Lead-Time.png)

There can be several lead times (e.g., customer lead time, development lead time, QA lead time, etc.) and specially the End to end Lead Time : The time in which a card goes from being created to being closed.  
This metric say about how the whole organization or product team (not only a development team) reacts to customer's needs.

Delivery/Cycle Lead Time : The time a card spend out of the backlog, ie. the elapsed time from the moment the team  starts actively working on a task till the moment they are done.  
This metric basically say about how responsive the team is or how fast they can deliver something when priorities change.

![](figure/Cycle-Time.png)

Different teams will use different definitions for start and done ("accepted by the product owner" vs "delivered to production").


### Cumulative Flow Diagrams

This report represents the relative amount of work for each stage of project over the time.
The key data points of the CFD are:

* The vertical distance between each area represents the amount of work in progress on the respective stage in a specific date
* The horizontal distance between the areas in the chart corresponds to the average lead time of the requests that arrived on a specific date
* The mean delivery rate, represented by the slope of the closed items area, corresponds to the trend in the delivery of the work.


This metric help understand the state of current work  and what might need to be done to speed up the pace of delivery.  
The diagram should run smoothly. Large steps and flat horizontal lines indicate impediments to flow or lack of flow. Variations in the gap or bands stand for bottleneck situations, which usually occur due to irrelevant work in progress limits.

![](figure/CFD.PNG)

### Lead Time Average

This report shows a trend of the average number of days a task took to be completed, from start to finish. It is categorized by work item type so teams can see the how the system is performing over time, broken down by work item type. 

### Flow Efficiency 

This report shows the average percentage of lead time that a developer spent working on a task (touch time). This shows the potential for process improvements. 


### Cycle time diagram
Stacked bar chart representing how much time a task has spent in a given state through is life-cycle, allowing the detection of tasks that are taking too long.

![](figure/cycle-time-column-2.png)

### Due Date Performance 

This report shows the percentage of items that were delivered on time and the average percentage delivery rate over time. This is useful for illustrating how predictable the system is. Due date performance with a low percentage provides evidence that there is an abundance of variability in the flow. The team should take corrective action or they will not be able to establish reasonable service agreements. 

 
### Bugs per Story 

This report shows a trend of the average number of defects opened against a Story. Attaining predictability is a fundamental aspect in the Kanban system, however, that will be ineffective if the software is delivered with low quality. This chart is also useful when implementing Kanban to help teams establish goals in the quality area. 

### Lead Time Distribution 

  This report is a statistical distribution that shows the number of occurrences by lead time. It is an effective way to identify discrepancies in the process and boosts the confidence of teams in the definition of service level agreements, based on real life data. 

### Throughput Trend 

   This report shows the number of items that were delivered in a given time period (eg monthly). It can be used to identify a trend of how well the system has been performing. As teams work on process improvements, the throughput trend will show a more consistent slope in the chart. 

![](figure/TroughputTrend.PNG)


<!--
## Kanban Strategies:
a kanban by project?
a kanban by team? a kanban by team seems more appropriate as one of the goal is to improve collaborative work.  
Team kanban can be combined with techniques like user map stories which allow to visualize project big pictures. 


### Six Rules for an Effective Kanban System

To ensure a proper setup of Kanban in the workplace, Toyota has provided us with six rules for an effective Kanban system:  
Customer (downstream) processes withdraw items in the precise amounts specified by the Kanban.  
Supplier (upstream) produces items in the precise amounts and sequences specified by the Kanban.  
No items are made or moved without a Kanban.  
A Kanban should accompany each item, every time.  
Defects and incorrect amounts are never sent to the next downstream process.  
The number of Kanbans is reduced carefully to lower inventories and to reveal problems.  
-->

Some Links:

* Explain Kanban practices with a game [Kanban Pizza Game](http://www.agile42.com/en/training/kanban-pizza-game/)
* Kanban Board App [Trello](http://trello.com)
* Kanban Board App [Restyaboard](http://restya.com/board/)

Sources:

[Kanban from the Inside: 20. Model workflow](http://positiveincline.com/index.php/2015/06/kanban-from-the-inside-20-model-workflow/)  
[Kanban Story](http://blog.crisp.se/2009/06/26/henrikkniberg/1246053060000)  
[Kanban Metrics: Measure Cycle Time To Stay Lean](http://blog.assembla.com/AssemblaBlog/tabid/12618/bid/102123/Kanban-Metrics-Measure-Cycle-Time-To-Stay-Lean.aspx)  
[7 LEAN METRICS TO IMPROVE FLOW](http://leankit.com/kanban/lean-flow-metrics/)  
[Improve predictability and efficiency with Kanban metrics using IBM Rational Insight](https://jazz.net/library/article/1350)  
[A brief introduction to kanban](https://www.atlassian.com/agile/kanban)
[Cumulative Flow Diagram](http://brodzinski.com/2013/07/cumulative-flow-diagram.html)
[Stack Exchange : What are commonly tracked metrics in kanban?](http://pm.stackexchange.com/questions/10657/what-are-some-commonly-tracked-metrics-in-kanban)
[Kanban Analytics part II: Cycle Time](http://blog.kanbanize.com/kanban-analytics-part-ii-cycle-time/)
[Agile Rambling - Tag Archives: metrics](http://agileramblings.com/tag/metrics-2/)
[Designing Your Kanban Board to Map Your Process](http://leankit.com/blog/2014/02/map-your-process-with-kanban)

