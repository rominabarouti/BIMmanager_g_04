# Introduction 

This project consisted of 5 sub assigments, and was aimed at utilizing OpenBIM to build a smart tool that uses data to improve construction operations and project reporting. In the first assignment, BIM analyst groups checked simple claims made in different project reports using ifcopenshell. The scripts were collected and validated by us, BIM Managers, under one main file [here](https://github.com/rominabarouti/BIMmanager_g_04/blob/main/main.py). The second sub assignment aimed at designing and proposing an OpenBIM tool. The idea and flow charts of the proposed tool is available [here](https://github.com/rominabarouti/BIMmanager_g_04/blob/main/A2/README.md). In short, our proposed tool aims at estimating CO2 emissions of a building using IFC models, ifcopenshell and additional external data sources. 

In the third assignment, the tool was fully developed and implemented using python and ifcopenshell. The scripts and related data sources are available [here](https://github.com/rominabarouti/BIMmanager_g_04/tree/main/A3). A [video walkthrough](https://youtu.be/JVlfLT0Y1Ok) of the code and the [Jupyter Notebook](https://github.com/rominabarouti/BIMmanager_g_04/blob/main/A4/CO2_tool_notebook.ipynb) depicting the development process of the code was provided in assignment 4 [here](https://github.com/rominabarouti/BIMmanager_g_04/blob/main/A4/README.md). Additional descriptions of the code can be found [here](https://github.com/rominabarouti/BIMmanager_g_04/blob/main/A4/README.md). In this final assignment, we reflect on the learnings of this course and provide perspective of OpenBIM both as a group as well as individuals in the following sections.  

# Learning Experience (Zahra & Fabiana)

**Identify Your Own Level at the Beginning of This Course and Where You Ended** 

Our level of knowledge regarding OpenBIM and IFC models was relatively basic, at the beginning 
of the course. We had a foundational understanding of BIM from our architecture background, 
but we were not familiar with techniqus to analyze, validate and extract information from BIM data, 
utilizing tools like Python, BonsaiBIM, and ifcOpenShell. By the end of the course, we have gained 
an intermediate proficiency in using Python, analyzing IFC model data, and an understanding of 
building sustainability assessment. 

**What Else Do You Still Need to Learn?** 

Despite our progress, we still need to deepen our understanding of more advanced scripting techniques 
for handling complex data from IFC models, particularly when working with incomplete datasets. We 
also need to explore more about other OpenBIM tools into our workflows, particularly in professional 
environments where clean and standard data is difficult to obtain.  

**How Might You Use OpenBIM in the Future?** 

We plan to integrate OpenBIM tools extensively into our future work, particularly in sustainable 
design and construction. This course has enabled us to tackle on a real-world challenge within 
construction and sustainability using a set of OpenBIM tools that should have prepared us to take
on similar challenges in a professional environment. OpenBIM is a broad field that is constantly 
evolving, which means any future use demands consistent exploration, development, and learning how 
to utilize AI to enhance performance.


# Process of developing the Tutorial (Zahra ,Fabiana)

**Did the Process of the Course Enable You to Answer or Define Questions 
That You Might Need Later for Thesis?** 

Yes, the course enabled us to address several questions related to the validation of 
sustainability claims in building designs. Specifically, it helped define the necessary 
tools and processes for validating CO2 emissions, which can be central to our future thesis 
work on sustainable construction. It also provided clarity on how to automate data 
extraction and analysis from BIM models, which could prove to be valuable for our research. 

**Would You Have Preferred to Have Been Given Less Choice in the Use Cases?**

While having a variety of use cases allowed us to explore different aspects of OpenBIM, 
we think a more focused approach could have helped us dive deeper into specific topics. 
Given the complexity of the tasks, fewer use cases with more detailed guidelines might 
have streamlined the process and allowed for more specialized learning. 

**Was the Number of Tools for the Course Ok? Should We Have More or Less? If So Which Ones Would You Leave Out?** 
The number of tools introduced in the course was appropriate. We used Python, BonsaiBIM, 
and ifcOpenShell. Each tool served a specific function that enhanced our ability to extract, 
manipulate, and analyze data from IFC models. However, we would consider streamlining the 
course by potentially omitting Blender/Bonsai, as its use was mainly for visualization, 
while Python and ifcOpenShell were more central to the tasks at hand. 

# Summary of the Feedback (Zahra & Fabiana)

As part of Group 4, we developed a tool that calculates the volume of building elements 
and links this to CO₂ emissions based on the materials used. The purpose of our tool is to 
provide an early estimate of a building's environmental impact during the design phase, 
making it easier to assess if the building could meet sustainability certifications before 
construction begins. This feedback recognized the tool as highly practical and potentially 
valuable in real-world applications, especially in promoting more sustainable design practices.

During our work, we encountered challenges in matching materials to building 
elements in the models. This was largely due to incomplete or missing material data, which 
required us to make some assumptions. The reviewers noted that such issues might be less 
prominent in professional projects, where models are typically more detailed and
complete. However, they emphasized the importance of establishing better IFC modeling guidelines 
to ensure all building elements are consistently assigned material and quantity data. 
Without this, there's a risk of relying on estimations, which could undermine the tool's 
accuracy and purpose.

The reviewers appreciated the potential of our tool as an initial LCA (Life Cycle Assessment) 
tool during the modeling phase, recognizing that it addresses a pressing need in the industry. 
They found our presentation engaging and relevant, praising the tool's applicability and its 
ability to tackle a critical problem in sustainable building design. Overall, the feedback 
highlighted our tool's promise and the quality of our work. 

# Your Future for Advanced Use of OpenBIM (Individual Parts)

**Are You Likely to Use OpenBIM Tools in Your Thesis? (Zahra Barouti)**

Yes. Throughout my past career as a BIM modeller and coordinator, I have not only gained experience working on BIM projects, but also have had a growing desire to expand my knowledge within this field. I am planning to focus my thesis on BIM and digitalization and with the learnings from this course, I am prepared to integrate OpenBIM tools into my thesis.   

**Are You Likely to Use OpenBIM Tools in Your Professional Life in the Next 10 Years? (Zahra Barouti)**

Yes. As previously stated, using OpenBIM tools is a natural path to developing my future career 
provided my personal interest and past work experience. In addition, considering the fast-paced 
growth of digital and AI-powered tools within the construction industry, using OpenBIM tools 
seems like an inevitable choice.  

**Wrap up, the journey through A1-A5 (Zahra Barouti)** 

*A1*: The learning experience for the first module was interesting in two ways. I was given a chance, for the first time, to get a high level view of an IFC model using different tools, namely BonsaiBIM and ifcopenshell. While BonsaiBIM was initially used to practice information extraction without needing to use code, ifcopenshell eventually helped us achieve a far higher flexibility in information extraction. Moreover, having taken the role of BIM Manager, I had 
the opportunity to experience the workflow of a manager by providing support to other team members and take on the responsibility to identify and resolve inconsistencies and discrepancies in results provided by the BIM analysts. The procedure involved continuous communication with different analyst groups to ensure assignments were aligned with the specified guidelines in the course, organizing sub modules in the manager repository and gluing everything together through importing and running everything in the main python file.  

*A2*: The opportunity to create an idea from scratch and develop it into actionable steps is
invaluable in growing a solution-oriented mindset. With the help of BPMN, I could easily iterate through different paths the idea could go and translate my thought process into a flow chart with minimal technical requirements. Also, I was excited to work on a sustainability related focus area as I see it a key factor in the future of construction industry. The idea eventually involved analysing the life cycle environmental impacts of materials (i.e. CO2 emissions) for each element used in a building that can provide a quick overview of the carbon footprint with minimal effort by the project manager discipline.

*A3*: This module was perhaps the most technically demanding stage throughout the course. I had to put an immense effort to improve my skills with python programming, especially using ifcopenshell to interact with an ifc file. This demanded a great deal of research and trial and error to obtain the desired goal. The additional challenge I faced throughout the development process was realizing the limitations in the data or the available tooling to achieve certain goals. Eventually, the developed tool became a python class that uses IFC files from various disciplines along with additional assumed data sources as input, and using several methods, it calculates and visualizes the CO2 emission of different IFC elements. An object-oriented approach was used for this tool to make further development of the tool simpler and also simplify usage of the tool by the end user. 

*A4*: A critical step was to provide clear description of the methodology and instruction for using the tool. This was done in different ways in this module. I took the opportunity to create a walkthrough video of my tool and made it publicly available on YouTube. Providing a clear and concise description of how everthing is tied together in the tool was itself a challenge but essential. While the video demonstrates the final object-oriented tool, I provided a Jupyter notebook that focuses more on the development process of the tool. It is worth noting that Jupyter notebook was the main tool used to develop the first working version of the our tool. A summamry of the tool and usage instruction with sample code snippets are also provided in the README file for this module. 

*A5*: This final module is a good practice to take a step back from the learnings and experiences of the course to gain a better perspective of what value the course has offered for me and what I have been able to learn and takeaway upon concluding it.    

**Are You Likely to Use OpenBIM Tools in Your Thesis? (Fabiana)** 

Yes, I am likely to incorporate OpenBIM tools into my thesis, as they are essential for assessing and validating the environmental  impacts of building designs. With a strong focus on sustainability in my research, OpenBIM  will play a critical role in analyzing CO₂ emissions and ensuring compliance with diverse standards across different countries. Having lived in multiple countries, I have observed the variation in building codes and sustainability requirements, and OpenBIM provides a platform to navigate and  harmonize these differences effectively. This aligns perfectly with my academic and professional focus on sustainable construction practices. 



**Are You Likely to Use OpenBIM Tools in Your Professional Life in the Next 10 Years? (Fabiana)**

Yes, I expect to rely heavily on OpenBIM tools in my professional life over the next decade as sustainability and data-driven decision making continue to grow in importance in the architecture and construction industry. OpenBIM's flexibility and collaborative potential make it an invaluable asset in streamlining workflows, improving project accuracy and ensuring compliance with increasingly stringent environmental regulations and sustainability goals. As a professional focused on sustainable construction, I see OpenBIM as a key enabler for integrating Life Cycle Assessments, monitoring CO₂ emissions and adapting projects to different global standards. Its ability to support interdisciplinary collaboration will also be critical in delivering innovative and efficient solutions for sustainable building design and construction. 

**Wrap Up (Fabiana)**

This journey through the OpenBIM tasks (A1-A5) has been an educational experience. It 
has allowed me to develop my knowledge and practical skills in using OpenBIM tools for claim validation and sustainability analysis. I started with a basic understanding of BIM and have now progressed to the point where I am able to apply these tools effectively to real-world design challenges. The hands-on work, from automating data extraction in Python to developing a CO2 calculation tool, has given me a solid foundation for using OpenBIM academically and professionally. 

*A1: First Assignment*

The Advanced Building Design course's OpenBIM assignment required using OpenBIM tools,
 specifically the IFC model, to verify a claim in a project report. The purpose was to show how a rule-checking procedure could be used to verify a tall building design claim. As manager, my duties included managing the team, supervising the validation procedure, and guaranteeing adherence to OpenBIM goals and standards. Our group concentrated on confirming a particular assertion about the building's Gross Floor Area (GFA) that was made in the client report. By examining the relevant data in the IFC model, the goal was to verify this assertion. In the first week of the validation process, we used Blender with the Bonsai plugin to review the disciplinary IFC models. We were able to visualize the building and comprehend its structure as a result. In the second week, we created a Python script in Blender to automatically extract important data from the IFC model, like the GFA. The script was created to look for pertinent properties and gather the information needed to compare the claim. We finished the assignment in week three by executing the script, evaluating the outcomes, and recording the procedure in the GitHub repository. The assignment presented several difficulties. 
 
 The complexity of the IFC data model was one of the primary problems. The task was initially time-consuming because it required knowledge of the IFC schema to extract specific information, like GFA. Furthermore, we had to troubleshoot the Blender/Bonsai plug-in due to technical issues in order to make sure the scripts operated as intended. The accuracy of our validation could have been impacted by missing or inconsistent data in the model, so data quality was also a concern. But we managed to get past these obstacles and continue working on the project. We verified that the claim was correct after executing the script and contrasting the extracted GFA value with the report's assertion. This successful validation showed the potential of automated rule checking procedures in building design workflows as well as the strength of OpenBIM tools in confirming claims. In conclusion, this assignment gave me a great chance to use OpenBIM standards in a practical setting. The process of creating and running scripts to retrieve data from the IFC model reaffirmed how crucial technical proficiency, teamwork, and meticulousness are to BIM project management. 

*A2: Second Assignment*

Our team was tasked with defining a use case for a fact-checking tool in a particular 
focus area for our second assignment. Our primary goal as managers is to guarantee that the CO2 emissions for every component of the building are precisely determined and adhere to the EN15978 standard. This is necessary to meet the project's environmental goals and verify the building design's sustainability. Building #2406 from the Advanced Building Design course last year has been selected as our case study in order to accomplish this. The assertion that we are looking into is found on page 20 of the report and concerns the environmental impact of materials over their life cycle, particularly the CO2 emissions of individual building components. According to the report, these emissions fall within the EN15978 standard's bounds. By computing the CO2 emissions of the building components using information from the IFC model and contrasting them with the stated values, we hope to confirm this. The first step in the process is to confirm that the IFC model accurately depicts the building's components, including the walls, floors, and windows. After confirming that the input data is accurate, we use EN15978 guidelines to calculate the CO2 emissions for each element and compare the results with the report's claims. Because choices made during the design stage have a big influence on the building's overall carbon footprint, early verification is essential. 

According to the report, these emissions fall within the EN15978 standard's bounds. By computing the CO2 emissions of the building components using information from the IFC model and contrasting them with the stated values, we hope to confirm this. The first step in the process is to confirm that the IFC model accurately depicts the building's components, including the walls, floors, and windows. After confirming that the input data is accurate, we use EN15978 guidelines to calculate the CO2 emissions for each element and compare the results with the report's claims. Because choices made during the design stage have a big influence on the building's overall carbon footprint, early verification is essential. One crucial step is to extract data from IFC classes like IfcElement, IfcQuantity, and IfcMaterial. Because Visual Studio Code supports Python and makes it simple to integrate the required packages, we'll be using it for development. The tool is very beneficial to society and business. It offers a rapid and precise method for evaluating sustainability early in the design process, improving decision-making and lessening the negative effects of construction on the environment. We can help create greener cities and cleaner buildings by assisting designers in putting sustainability first from the beginning. By automating intricate calculations and guaranteeing adherence to environmental regulations, this brief illustrates how OpenBIM tools can improve the efficiency, transparency, and sustainability of the building design process.

*A3 & A4: Third and fourth Assignment*

In this assignment, we set out to create a tool to calculate the CO₂ emissions of building elements by analysing IFC models for architecture, structure, and MEP. This process required integrating data management, programming, and sustainability principles into a integrated workflow, which was both a technical challenge and a good learning experience. We started by importing IFC models and identifying a variety of building elements such as walls, roofs, beams or columns. One of the first challenges we encountered was the incomplete material data for most of the elements in the IFC models. This gap forced us to make educated assumptions about the materials based on the types of building elements. While this approach allowed us to move forward, it highlighted the limitations of working with incomplete data sets and the importance of having robust, standardized data in IFC models 
 – which will hopefully be more complete in a professional work environment. 
 
 To organize the data, we used a JSON file to record the assumed materials and key geometric properties such as length, area and volume. This step taught us the importance of structuring data in a way that is both accessible and adaptable. By importing the JSON data into Python, we were able to process it and calculate the CO₂ emissions for each building element using the EN15978 standard. This part of the project deepened our understanding of how to integrate environmental assessment standards into practical workflows. A key insight was the extent to which the geometry and material properties of building elements influence their CO₂ emissions.
     
By extracting geometric properties directly from the IFC model - combined with our assumed material data - we were able to quantify emissions on a volume, area or length basis. The results were organized into a table that categorizes the types of elements, its geometric dimensions and the calculated CO₂ emissions. To make the results more accessible, we created a pie chart in Python that visually represented the percentage contribution of each element type to total CO₂ emissions. This visualization is an important to show how complex data effectively. Such charts show which building components had the greatest environmental impact which should influence design decisions. 

Throughout the process, we faced some challenges. The lack of explicit material data in the IFC models was a recurring issue, and while our assumptions were practical for this exercise, they highlighted the importance of better modelling practices and standards. This experience taught us that data accuracy and reliability are critical to accurate sustainability assessments, and that improving the completeness of IFC's models could significantly enhance their usefulness. Beyond the technical aspects, this project demonstrated the potential of digital tools such as OpenBIM and Python to advance sustainable construction practices. By developing a tool to automate CO₂ emissions calculations, we gained a deeper understanding of how programming and data analysis can support environmentally responsible decision-making. This assignment was an opportunity to explore how technology can address real-world sustainability challenges. It reinforced the importance of collaboration, critical thinking and continuous learning in solving complex problems. 

