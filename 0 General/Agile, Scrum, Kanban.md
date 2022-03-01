# The Agile Methodology

<details>
  <summary>Table of Contents</summary>

  - [What is Agile?](#what-is-agile)
  - [Why Agile?](#why-agile)
  - [Scrum/Kanban](#scrumkanban)
    - [Benefits of Agile:](#benefits-of-agile)
  - [Scrum](#scrum)
    - [Roles](#roles)
    - [Terminology](#terminology)
    - [Workflow](#workflow)
  - [Kanban](#kanban)
    - [Visualize Work](#visualize-work)
    - [Limit Work-in-Progress](#limit-work-in-progress)
  - [Similarities and Differences](#similarities-and-differences)
    - [Workflow](#workflow-1)
    - [Roles and Responsibilities](#roles-and-responsibilities)
    - [Commitment](#commitment)
    - [Planning](#planning)
    - [Workload](#workload)
    - [Modifications / Changes](#modifications--changes)
    - [Performance Indicators](#performance-indicators)
    - [Project Boards](#project-boards)
    - [Application](#application)
  - [Summary](#summary)
  - [Resources](#resources)

</details>

## What is Agile?

"Agile" is an umbrella term for a set of frameworks and practices that break down complex projects into small, manageable goals.

This philosophy can take on many forms, but the most common two are **Scrum** and **Kanban**.

## Why Agile?

The Agile development mentality was created as an alternative to the **Waterfall** method of development.

The Waterfall Method follows these steps:

1. Planning and Design
2. Code
3. Test
4. Release

This can work well, but often there are unforeseen challenges in the Coding stage that will send the entire project back to the Planning or bugs in the Testing phase which will send the entire project back to the Coding phase. This can cause a delay in the release of a product, this causing the release of an outdated product.
### Benefits of Agile:
- Quickly adapts to changing requirements
- Very flexible
- Faster product launches
- Faster decision-making
- Improved team communication
- Emphasis on continuous analysis and workflow improvement
## Scrum/Kanban

Built around the Agile Methodology, **Scrum** and **Kanban** offer alternatives to the Waterfall Method. They each aim to break a complex task down into smaller, more manageable pieces that each pass through the Design, Coding and Testing phases before their individual releases. 

This will lead to faster and more frequent feature releases and ensure that each is adapted to the ever-changing needs of the project and the market.


[Back to Top](#the-agile-methodology)

## Scrum

Scrum teams commit to shipping working software through set 2-4 week intervals called **sprints**. Their goal is to release working software quickly and incrementally and to create learning loops based by regularly reviewing the process and making improvements.

### Roles

Scrum teams are separated into three distinct roles:

1. Product Owner - The person with the idea for the product
2. Scrum Master - Project manager who acts as a liasson between the Product Owner and the Team to ensure the features being released are meeting expectations.
3. Scrum Team - Designers, developers and anyone else that works to complete each phase of the project.

### Terminology

**User Story** - A way of describing a feature set. Helps estimate the size of the sprint. Follows the formula:
    
> "As ___ I need ___ so that ___." 
    
Describes to the product owner what features need to exist and how they'll be used.

**Sprint** - Limited timeframe to complete a feature as described in a User Story (usually 2-4 weeks)

### Workflow

**1. Product Backlog** - Product owner's list of desired features that could go into the product. The Product Owner prioritizes the list and brings it to the Scrum Master / Team.

**2. Sprint Planning** - Product Owner and Scrum Master discuss the desired features and determine which user stories can/should be accomplished in the next sprint.

**3. Sprint Backlog** - Output of Sprint Planning. A list of user stories which have been committed to the next sprint. 

**4. Sprint** - Limited timeframe (usually 2-4 weeks) to accomplish the work from the Sprint Backlog. Daily Scrum Meetings keep everyone on task and determine potential roadblocks to completing the user stories. Once a sprint it started, no additional requirements can be added to the sprint.

**5. Potentially Shippable Product** - The outcome of a sprint. The Product Owner will decide if its ready to ship or if additional features are needed.

**6. Sprint Review/Retrospective** - Team demonstrates the new features to the product owner and discusses how to improve the process in the future.
   
**7. Repeat for each new feature**

[Back to Top](#the-agile-methodology)

## Kanban
Kanban focuses on a continuous workflow by visualizing all the work that needs to be done and limiting the amount of work in progress at any one time. This is usually done with the help of a "Kanban Board" which separates the work into categories like "To Do", "In Progress", "Code Review" and "Complete".

The success of a Kanban workflow is measured on how quickly tasks go from the "To Do" column to the "Complete" column. This is know as the "Cycle Time"

Kanban follows two main philosophies: Visualize Work and Limit Work-in-Progress

### Visualize Work

All the work required for a project is collected and written on cards which are placed on a Kanban board.

Kanban Board is split into 3 categories: 
  - To Do
  - In Progress
  - Done

The entire team can see and interact with the board

### Limit Work-in-Progress

Tasks are moved from the To Do column to the In Progress column as needed to meet changing project requirements. Only a limited number of tasks can be In Progress at any one time, so as not to overload the team. 

[Back to Top](#the-agile-methodology)

## Similarities and Differences

### Workflow
|Scrum|Kanban|
|-|-|
|**Sprint** - Time limit of one month or less during which the team produces a potentially shippable product increment|**Flow** - No required timeframes. Focuses on maintaining a continuous workflow and continuous delivery by limiting the amount of work in progress.|

### Roles and Responsibilities
|Scrum|Kanban|
|-|-|
|Has a set of mandatory roles, each with its own responsibilities: **Product Owner**, **Scrum Master**, **Scrum Team** |No set roles are prescribed. There might be an **Agile Coach** to keep team members on track, but no one manages the Agile workflow explicitly.|

### Commitment
|Scrum|Kanban|
|-|-|
|Team commits to a specific amount of work for each iteration. If the amount of work is not measured accurately, a Sprint may fail.|Work is based on capacity. Work-in-Progress limits prevent team members from working on multiple tasks.|

### Planning
|Scrum|Kanban|
|-|-|
|Planning happens iteratively at the beginning of each Sprint|Almost no planning. Implements "Just-in-Time" planning, which aims to supply features just as they're needed|

### Workload
|Scrum|Kanban|
|-|-|
|Limits work-in-progress based on the needs of the current Sprint. Everything for a Sprint could be worked on simultaneously if needed. |Limits the number of active tasks in each column of the Kanban board. No new tasks can be assigned to a column until another task leaves that column.|

### Modifications / Changes
|Scrum|Kanban|
|-|-|
|Once a Sprint begins, no new requirements can be added.|Tasks can be added to the backlog at any time. Tasks can be started or paused based on changing prioritization. Work-in-Progress limits still apply.|

### Performance Indicators
|Scrum|Kanban|
|-|-|
|Productivity is measured by **velocity**, which is the number of story points completed in a sprint.|Productivity is measured by **Lead Time** which is the total time required to complete a project and **Cycle Time** which is the amount of time it takes a particular task to pass from the "To Do" column to the "Completed" column|

### Project Boards
|Scrum|Kanban|
|-|-|
|All tasks for a Sprint should be in the "Completed" column by the end of that Sprint. Board is reset after every Sprint Review.|Each column has a Work-in-Progress limit. The maximum number of item in each column can't exceed that number. Items stay in their columns until they are able to be moved. There are no timeframes so the board continues as long as the project continues and is never reset.|

### Application
|Scrum|Kanban|
|-|-|
|Ideal for fast-moving projects that need some degree of coordination in planning or goal-driven projects that have fixed deliverables. Suitable for non-mature teams due to strict guidelines and timeframes.|Best suited for projects that change frequently or have many incoming tasks. Better suited for more mature, self-guided teams.|

## Summary
||Scrum|Kanban|
|-|-|-|
|**Cadence**|Regular, fixed-length sprints|Continuous flow|
|**Release Methodology**|At the end of each Sprint|Continuous Delivery|
|**Key Metrics**|Velocity|Lead and Cycle Time, Work-in-Progress limits|
|**Roles**|Product Owner, Scrum Master, Development Team|No required roles|
|**Teams**|Cross-functoinal|Can be specialized|
|**Modifications**|Changes during a Sprint are strongly discouraged|Can happen at any time|
|**Work-in-Progress Limits**|Limits Work-in-Progress per Sprint|Limits Work-in-Progress based on task limits on each column of the work board|
|**Commitment**|Teams are required to commit to a specific amount of work|Commitment not necessary and is optional for teams|
|**Storyboard**|Board is reset after each Sprint|Board is persistent for the duration of the project

[Back to Top](#the-agile-methodology)

## Resources
[Agile Manifesto](https://agilemanifesto.org/)

[Scrum Guide](https://scrumguides.org/scrum-guide.html)

[Kanban Guide](https://kanbanguides.org/)

[Scrum Vs Kanban](https://www.wrike.com/blog/scrum-vs-kanban/#What-is-Scrum)