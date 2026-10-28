<div align="center">

<img src=".github/assets/profile-flight-deck.svg" alt="Denis7Kom — software, interactive systems and application security" width="100%" />

<p><strong>Software · Interactive Systems · Application Security</strong></p>

<p>
<a href="#featured-work"><img src="https://img.shields.io/badge/EXPLORE%20PROJECTS-35D0BA?style=for-the-badge&amp;logo=github&amp;logoColor=0D1117" alt="Explore projects" /></a>
<a href="#cybersecurity"><img src="https://img.shields.io/badge/SECURITY%20FOCUS-F5C451?style=for-the-badge&amp;logo=letsencrypt&amp;logoColor=0D1117" alt="Security focus" /></a>
<a href="https://denis7kom.github.io/denis-komarov/"><img src="https://img.shields.io/badge/VISIT%20PORTFOLIO-8B5CF6?style=for-the-badge&amp;logo=firefoxbrowser&amp;logoColor=white" alt="Visit portfolio" /></a>
</p>

<p>
<a href="#featured-work">Projects</a> &nbsp; / &nbsp;
<a href="#cybersecurity">Security</a> &nbsp; / &nbsp;
<a href="#toolkit">Toolkit</a> &nbsp; / &nbsp;
<a href="#github-overview">Activity</a> &nbsp; / &nbsp;
<a href="#connect">Connect</a>
</p>

</div>

<br />


## whoami

<img src=".github/assets/profile-whoami-v5.svg" alt="Animated Denis7Kom developer console with identity, current focus, application-security learning and engineering workflow" width="100%" />

<details>
<summary><b>$ inspect --identity</b> — developer profile &amp; current focus</summary>

I build **software applications and interactive systems** with attention to behaviour, data flow and visual structure. Alongside software engineering, I study **application security**, especially trust boundaries, access control and verification.

| Engineering lens | What it means in practice |
| :--- | :--- |
| **Build** | Understand the user journey, model the data and implement readable behaviour. |
| **Experience** | Use movement, visual feedback and meaningful interaction rather than decoration alone. |
| **Security** | Question assumptions, inspect permissions and test what happens when requests fail. |
| **Improve** | Observe results, revise the implementation and document relevant trade-offs. |

</details>

<details>
<summary><b>$ cat ./current-quest</b> — learning &amp; iteration</summary>

<img src=".github/assets/lab-status.svg" alt="Animated development quest" width="75%" />

**Working approach:** understand the problem → model the states → build → verify → refine.

Focus areas describe projects, interests and ongoing learning, not unsupported claims about seniority or proficiency.

</details>

## What I Build

<img src=".github/assets/build-tracks-v3.svg" alt="Animated overview of software applications, interactive visual systems and security foundations" width="100%" />

<sub>Click a topic to expand a technical view. These are areas of work and study, not a claim of equal proficiency in every technology.</sub>

<details>
<summary><b>01 / Applications</b> — interface → request handling → persistence</summary>

**I build around behaviour, not just screens.** A feature is the full path from user interaction through business logic to stored data.

- **Frontend:** accessible navigation, responsive layouts, meaningful interaction states.
- **Backend:** request handling, validation, sessions, error paths and predictable business rules.
- **Data layer:** relational models, persistence and consistent state across user journeys.
- **Example:** in [VibeShop](https://github.com/Denis7Kom/website-turbo-layout), the customer journey connects JSP pages, Servlets, DAO classes and relational data.

`USER ACTION → CONTROLLER → DOMAIN LOGIC → DATABASE → RESPONSE`

</details>

<details>
<summary><b>02 / Interactive Systems</b> — visual logic, motion &amp; simulation</summary>

A convincing interactive experience needs more than visual effects: the behaviour, animation state and user controls must agree.

- Procedural geometry and interactive 3D scenes.
- Event-driven updates, transitions and state-dependent visuals.
- Controls designed for both desktop and mobile interfaces.
- Iteration on usability and performance, not only appearance.

`INPUT → UPDATE STATE → RENDER → FEEDBACK`

</details>

<details>
<summary><b>03 / Security Foundations</b> — boundaries, assumptions &amp; verification</summary>

My ongoing security learning focuses on the application's trust boundaries: where user-controlled input arrives, where identity is verified and where access must be checked.

- Track data from entry points to sensitive operations.
- Separate authentication (**who is the user?**) from authorisation (**can they access this object?**).
- Review failure paths and look for missing checks.
- Verify changes with positive **and** negative test cases.

`DEFINE BOUNDARY → FIND ASSUMPTION → TEST FAILURE → VERIFY FIX`

</details>


## Featured Work

<sub>SELECTED PROJECT / 01 — the only featured work on this profile.</sub>

<a href="https://github.com/Denis7Kom/website-turbo-layout"><img src=".github/assets/feature-vibeshop-v2.svg" alt="VibeShop — animated live-music e-commerce showcase with concerts, artists and merchandise" width="100%" /></a>

### VibeShop · Turbo Layout

A **Java web application for live-music commerce**, developed as a team project for the University of Salerno. It connects **concert and artist discovery** with a real e-commerce workflow: accounts, product selection, cart, checkout, order history and administrative management.

**Stack:** `Java` · `JSP` · `Servlets` · `HTML/CSS` · `SQL` · `DAO`

<img src=".github/assets/vibeshop-architecture-v3.svg" alt="VibeShop architecture: JSP frontend, Java Servlet controllers, DAO layer, relational SQL data and route guards" width="100%" />

<details open>
<summary><b>Explore the customer journey</b> — guest → member → order</summary>

| Stage | Behaviour |
| :--- | :--- |
| **Discover** | Browse concerts, artists and merchandise; search the catalogue. |
| **Account** | Register, sign in and access an individual profile. |
| **Select** | Add products to a cart and review the purchase. |
| **Checkout** | Complete an order as an authenticated customer. |
| **Track** | Review past orders and manage profile information. |

**Flow:** `DISCOVER` → `PRODUCT` → `CART` → `CHECKOUT` → `ORDERS`

</details>

<details>
<summary><b>Explore the admin view</b> — catalogue, events &amp; operations</summary>

The project includes a separate administration area for maintaining concerts and merchandise, reviewing orders and managing support requests.

The source tree contains dedicated administrative Servlets and an `AdminFilter`. Their presence documents the application's routing structure; it does **not** by itself establish that every authorisation path has been independently audited.

</details>

<details>
<summary><b>Under the hood</b> — explore real source files</summary>

| Layer | Implementation |
| :--- | :--- |
| **Views** | [JSP pages](https://github.com/Denis7Kom/website-turbo-layout/tree/main/VibeShop/src/main/webapp/jsp) for catalogue, cart, checkout, account and orders |
| **Request layer** | [Java Servlets](https://github.com/Denis7Kom/website-turbo-layout/tree/main/VibeShop/src/main/java/com/turbolayout) including `CartServlet`, `CheckoutServlet`, `LoginServlet` and `SearchServlet` |
| **Domain layer** | [Model classes](https://github.com/Denis7Kom/website-turbo-layout/tree/main/VibeShop/src/main/java/model) for users, products, concerts, cart items and orders |
| **Data access** | [DAO classes](https://github.com/Denis7Kom/website-turbo-layout/tree/main/VibeShop/src/main/java/model/dao) for user, artist, concert, product and order data |
| **Database** | [SQL schema](https://github.com/Denis7Kom/website-turbo-layout/blob/main/VibeShop/db/VIBESHOP_FINAL.sql) |
| **Access filters** | [AuthFilter / AdminFilter](https://github.com/Denis7Kom/website-turbo-layout/tree/main/VibeShop/src/main/java/filter) |

The university project is **completed**. Future refactoring and application-security hardening are listed as potential follow-up work, not finished features.

</details>

<p align="center">
<a href="https://github.com/Denis7Kom/website-turbo-layout"><img src="https://img.shields.io/badge/EXPLORE%20SOURCE%20%26%20DOCS-8B5CF6?style=for-the-badge&amp;logo=github&amp;logoColor=white" alt="Explore VibeShop source and documentation" /></a>
</p>

<sub>Team: Denis7Kom · Ivan Perruolo · Giulio Alessandro Peluso.</sub>


## Cybersecurity

<img src=".github/assets/security-path-v3.svg" alt="Animated application security map: trace input, check object access, review assumptions, and verify fixes" width="100%" />

I am building my **application-security knowledge** by connecting security concepts to actual software behaviour. The emphasis is on reproducible findings, clear trust boundaries and verifiable fixes.

<details>
<summary><b>01 / Threat modelling</b> — what can cross a trust boundary?</summary>

**Threat modelling** is the practice of identifying assets, entry points, trust boundaries and plausible failure scenarios *before* assuming a feature is safe.

Example: a browser sends an order ID to a Servlet. The server must establish whether the authenticated user is allowed to access that specific order—not merely whether they are logged in.

`USER INPUT → SESSION → OBJECT LOOKUP → OWNER CHECK → RESPONSE`

</details>

<details>
<summary><b>02 / Authentication &amp; authorisation</b> — identity is not permission</summary>

- **Authentication** establishes an identity, for example through a valid user session.
- **Authorisation** evaluates an action against an object and its owner or role.
- **IDOR/BOLA** describes missing object-level authorisation, such as reading another customer's order by changing an identifier.

In VibeShop, `AuthFilter` and `AdminFilter` are concrete code locations to study. A filter alone is not proof that every object-level permission has been enforced.

</details>

<details>
<summary><b>03 / Input &amp; data handling</b> — validate at each boundary</summary>

I focus on where untrusted input meets business logic and storage: parameter validation, SQL query construction, output encoding and error handling.

**Example review question:** when a search string reaches a DAO, is it safely bound as data rather than interpreted as query syntax? The answer requires inspecting the implementation, not trusting the UI.

</details>

<details>
<summary><b>04 / Reproduction &amp; regression tests</b> — demonstrate the fix</summary>

A useful security review produces evidence: initial conditions, a repeatable request, the observed result, the expected result and a test that prevents recurrence.

`REPRODUCE → IDENTIFY ROOT CAUSE → CHANGE CODE → RETEST → DOCUMENT`

**Status:** learning and exploring. These are focus areas and review methods, not claimed certifications, vulnerability discoveries or a completed audit of VibeShop.

</details>

## Toolkit

<p align="center"><em>Languages and tools across projects and ongoing exploration; depth varies by technology.</em></p>

<p align="center"><strong>Languages</strong><br />
<img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&amp;logo=openjdk&amp;logoColor=white" alt="Java" />
<img src="https://img.shields.io/badge/JavaScript-B99A00?style=flat-square&amp;logo=javascript&amp;logoColor=white" alt="JavaScript" />
<img src="https://img.shields.io/badge/C-566C9C?style=flat-square&amp;logo=c&amp;logoColor=white" alt="C" />
<img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&amp;logo=cplusplus&amp;logoColor=white" alt="C++" />
<img src="https://img.shields.io/badge/C%23-764ABC?style=flat-square" alt="C#" />
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/SQL-336791?style=flat-square" alt="SQL" />
<img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&amp;logo=gnubash&amp;logoColor=white" alt="Bash" />
<img src="https://img.shields.io/badge/PHP-777BB4?style=flat-square&amp;logo=php&amp;logoColor=white" alt="PHP" />
<img src="https://img.shields.io/badge/Ruby-CC342D?style=flat-square&amp;logo=ruby&amp;logoColor=white" alt="Ruby" />
<img src="https://img.shields.io/badge/Assembly-555555?style=flat-square" alt="Assembly" />
</p>

<p align="center"><strong>Web & Interactive Graphics</strong><br />
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&amp;logo=html5&amp;logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square" alt="CSS3" />
<img src="https://img.shields.io/badge/JSP-E76F00?style=flat-square" alt="JSP" />
<img src="https://img.shields.io/badge/Servlets-E76F00?style=flat-square" alt="Servlets" />
<img src="https://img.shields.io/badge/WebGL-990000?style=flat-square&amp;logo=webgl&amp;logoColor=white" alt="WebGL" />
<img src="https://img.shields.io/badge/Three.js-222222?style=flat-square&amp;logo=threedotjs&amp;logoColor=white" alt="Three.js" />
<img src="https://img.shields.io/badge/React-20232A?style=flat-square&amp;logo=react&amp;logoColor=white" alt="React" />
</p>

<p align="center"><strong>Workflow & Platforms</strong><br />
<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&amp;logo=git&amp;logoColor=white" alt="Git" />
<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&amp;logo=github&amp;logoColor=white" alt="GitHub" />
<img src="https://img.shields.io/badge/Node.js%20tooling-339933?style=flat-square&amp;logo=nodedotjs&amp;logoColor=white" alt="Node.js tooling" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&amp;logo=githubactions&amp;logoColor=white" alt="GitHub Actions" />
<img src="https://img.shields.io/badge/GitHub%20Pages-222222?style=flat-square&amp;logo=githubpages&amp;logoColor=white" alt="GitHub Pages" />
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&amp;logo=docker&amp;logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/Arduino-00878F?style=flat-square&amp;logo=arduino&amp;logoColor=white" alt="Arduino" />
<img src="https://img.shields.io/badge/PyCharm-000000?style=flat-square&amp;logo=pycharm&amp;logoColor=white" alt="PyCharm" />
</p>

## GitHub Overview

<p align="center"><sub>Public GitHub activity. Language charts describe repository composition.</sub></p>

<div align="center">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=Denis7Kom&amp;theme=github_dark" alt="GitHub profile statistics" width="47%" />
<img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Denis7Kom&amp;theme=github_dark" alt="Repositories by language" width="47%" />

<img src="https://streak-stats.demolab.com/?user=Denis7Kom&amp;theme=github-dark-blue&amp;hide_border=true" alt="GitHub contribution streak" width="70%" />

</div>


## My Build Pattern

<img src=".github/assets/build-loop-v3.svg" alt="Animated engineering feedback loop: understand requirements, model, implement, verify and refine" width="100%" />

The goal is a **repeatable path from a requirement to observable behaviour**, with enough evidence to know whether the implementation meets the intended contract.

<details>
<summary><b>01 + 02 / Understand &amp; Model</b> — requirements, states and boundaries</summary>

Start with the user journey and the system's constraints. Separate *what should happen* from *how it will be implemented*. Sketch state transitions, important data entities, expected errors and trust boundaries.

**VibeShop example:** product discovery → cart → authenticated checkout → order history. Each transition implies a request, a change of state or an access rule.

</details>

<details>
<summary><b>03 / Implement</b> — explicit responsibilities, readable code</summary>

Separate view rendering, request coordination, domain state and persistence. Prefer descriptive names and small responsibilities over clever abstractions without a clear benefit.

**VibeShop example:** JSP is the presentation layer; Servlets handle requests; model classes carry state; DAO classes interact with persistence.

</details>

<details>
<summary><b>04 / Verify</b> — successful paths, failures and edge cases</summary>

Review what happens when inputs are missing, an object does not exist, a session expires, permissions are insufficient or a request repeats. Validate the observable result rather than assuming a code change solved the problem.

**Example test cases:** empty cart; expired session during checkout; account A requesting account B's order.

</details>

<details>
<summary><b>05 / Refine</b> — performance, security &amp; documentation</summary>

Measure the actual bottleneck before optimising. Reduce complexity where possible, revisit exposed trust boundaries and document the trade-offs that future maintainers need to understand.

`OBSERVE → EXPLAIN → CHANGE ONE THING → VERIFY AGAIN`

</details>


## Beyond the Code

<img src=".github/assets/beyond-code-v1.svg" alt="Animated photography, aerial video and aviation illustration exploring composition, spatial movement and systems thinking" width="100%" />

**Different disciplines, shared habits:** composition, movement and precision influence how I approach software and visual projects. Expand a subject to explore its connection to engineering.

<details>
<summary><b>01 / Photography</b> — composition, light &amp; attention to detail</summary>

Photography is an exercise in deliberate choices: what belongs in the frame, what should stand out and what distracts from the subject.

**Connection to software:** the same discipline applies to visual hierarchy, spacing, contrast and interface clarity.

- **Composition → layout:** place important actions where users can find them.
- **Light & contrast → readability:** separate content and interface states without visual noise.
- **Editing → iteration:** compare alternatives and remove what does not communicate.

**Practical example:** a dashboard can show correct data but still be difficult to use when every element competes for attention.

[Drone & Camera portfolio](https://denis7kom.github.io/Denis-Komarov-PH/) · [Shutterstock photography](https://www.shutterstock.com/g/Denis+Komarov%20PH?rid=259170704)

</details>

<details>
<summary><b>02 / Aerial Video</b> — perspective, motion &amp; spatial storytelling</summary>

Aerial footage combines framing, movement and a changing point of view. Smooth camera work should help someone understand a scene rather than simply adding motion.

**Connection to software:** interactive 3D scenes, camera controls and motion design also depend on predictable movement and feedback.

- **Perspective → spatial reasoning:** understand objects in relation to their environment.
- **Camera movement → interaction:** keep orientation clear while the viewpoint changes.
- **Visual continuity → UX:** transitions should clarify what changed and where to look next.

**Practical example:** when a user rotates a 3D model, stable controls and a clear focal point matter more than elaborate effects.

[View aerial photography and video](https://denis7kom.github.io/Denis-Komarov-PH/)

</details>

<details>
<summary><b>03 / Aviation</b> — systems thinking, procedures &amp; precision</summary>

Aviation inspires my interest in interconnected systems, operational logic and interfaces that express changing states.

**Connection to software:** understandable systems make dependencies, control inputs and failure cases explicit.

- **Checklists → consistency:** document repeated steps and reviewable decisions.
- **Cockpit displays → information design:** present relevant information at the right time.
- **Aircraft systems → state modelling:** controls must correspond to coherent system states.
- **Procedures → verification:** distinguish intended behaviour from what happened.

**Practical example:** interactive aircraft models need consistent relationships between controls, flight surfaces, landing gear and the visible aircraft state.

[Interactive aviation project](https://denis7kom.github.io/denis-aviation/) · [GitHub source](https://github.com/Denis7Kom/denis-aviation)

</details>

<details>
<summary><b>04 / Writing</b> — structure, clarity &amp; documentation</summary>

Writing is another way to organise complex material into something understandable. Good documentation asks the same questions as good storytelling: what does the reader need to know first, which context is missing and how does the argument progress?

**Connection to software:** precise names, clear explanations and structured documentation make technical projects easier to understand and maintain.

[My books](https://www.amazon.it/stores/Denis-Komarov/author/B0CCSK74QC)

</details>

<p align="center">
<a href="https://denis7kom.github.io/Denis-Komarov-PH/"><img src="https://img.shields.io/badge/DRONE%20%26%20CAMERA-35D0BA?style=for-the-badge" alt="Drone and Camera portfolio" /></a>
<a href="https://www.shutterstock.com/g/Denis+Komarov%20PH?rid=259170704"><img src="https://img.shields.io/badge/PHOTO%20GALLERY-8B5CF6?style=for-the-badge" alt="Photography gallery" /></a>
<a href="https://denis7kom.github.io/denis-aviation/"><img src="https://img.shields.io/badge/AVIATION-F5C451?style=for-the-badge" alt="Interactive aviation project" /></a>
<a href="https://www.amazon.it/stores/Denis-Komarov/author/B0CCSK74QC"><img src="https://img.shields.io/badge/BOOKS-5D6C82?style=for-the-badge" alt="Author books" /></a>
</p>

## Connect

<div align="center">

<a href="https://github.com/Denis7Kom"><img src="https://img.shields.io/badge/GitHub%20%C2%B7%20Denis7Kom-0D1117?style=flat-square&amp;logo=github&amp;logoColor=white" alt="GitHub · Denis7Kom" /></a>
<a href="https://denis7kom.github.io/denis-komarov/"><img src="https://img.shields.io/badge/Portfolio%20%C2%B7%20Denis7Kom-8B5CF6?style=flat-square" alt="Portfolio · Denis7Kom" /></a>

<br /><br />

<img src=".github/assets/lab-quest.svg" alt="Pixel development quest: learn, build, test, repeat" width="100%" />

</div>
