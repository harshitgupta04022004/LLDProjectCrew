# #!/usr/bin/env python
# import sys
# import warnings
# import os
# from datetime import datetime
# import gradio as gr


# from lldproj.crew import LLDProjectCrew
# warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# # This main file is intended to be a way for you to run your
# # crew locally, so refrain from adding unnecessary logic into this file.
# # Replace with inputs you want to test with, it will automatically
# # interpolate any tasks and agents information

# diagram = """
# <diagram>
#   <classes>
#     <class name="Game" type="class">
#       <attributes>
#         <attribute visibility="-" name="Player" type="list&lt;player&gt;" />
#         <attribute visibility="-" name="Board" type="Board" />
#         <attribute visibility="-" name="Dice" type="dice" />
#       </attributes>
#       <methods>
#         <method visibility="+" name="StartGame" returnType="void" params="" />
#         <method visibility="+" name="PlayTurn" returnType="void" params="" />
#         <method visibility="+" name="CheckWin" returnType="void" params="" />
#       </methods>
#     </class>
#     <class name="Dice" type="interface">
#       <attributes>
#         <attribute visibility="-" name="Roll" type="int" />
#       </attributes>
#       <methods>
#       </methods>
#     </class>
#   </classes>
#   <relationships>
#     <relationship type="inheritance" source="Dice" target="Game" />
#   </relationships>
# </diagram>
# """
# user_input = "Please analyze the following UML class diagram and provide a detailed report on the structural validity, relationship correctness, and design quality of the classes and relationships."

# def run(diagram, user_input):
#     inputs = {
#         "diagram_input": diagram,
#         "user_input": user_input,      # Raw diagram JSON/XML or parsed intermediate representation

#     }
#     result = LLDProjectCrew().crew().kickoff(inputs=inputs)
#     # print("\n\n===Final Result===\n\n", result.raw)
#     return result


# def greet(name, intensity):
#     return "Hello, " + name + "!" * int(intensity)

# demo = gr.Interface(
#     fn=run,
#     inputs=["diagram_XML", "User_input"],
#     outputs=["json"],
#     api_name="LLD"
# )

# # demo.launch()

# if __name__ == "__main__":
#     demo.launch()



#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime
import gradio as gr
import json

from lldproj.crew import LLDProjectCrew
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

default_diagram = """<diagram>
  <classes>
    <class name="Game" type="class">
      <attributes>
        <attribute visibility="-" name="Player" type="list&lt;player&gt;" />
        <attribute visibility="-" name="Board" type="Board" />
        <attribute visibility="-" name="Dice" type="dice" />
      </attributes>
      <methods>
        <method visibility="+" name="StartGame" returnType="void" params="" />
        <method visibility="+" name="PlayTurn" returnType="void" params="" />
        <method visibility="+" name="CheckWin" returnType="void" params="" />
      </methods>
    </class>
    <class name="Dice" type="interface">
      <attributes>
        <attribute visibility="-" name="Roll" type="int" />
      </attributes>
      <methods>
      </methods>
    </class>
  </classes>
  <relationships>
    <relationship type="inheritance" source="Dice" target="Game" />
  </relationships>
</diagram>"""

default_user_input = "Please analyze the following UML class diagram and provide a detailed report on the structural validity, relationship correctness, and design quality of the classes and relationships."

def run(diagram, user_input):
    inputs = {
        "diagram_input": diagram,
        "user_input": user_input,
    }
    result = LLDProjectCrew().crew().kickoff(inputs=inputs)
    output = result.raw if hasattr(result, "raw") else str(result)
    output = output.replace("```json", "").replace("```", "").strip()
    parsed = json.loads(output)
    if isinstance(parsed, str):
        parsed = json.loads(parsed)

    return parsed


demo = gr.Interface(
    fn=run,
    inputs=[
        gr.Textbox(
            label="Diagram XML", 
            value=default_diagram,
            lines=20,
            placeholder="Paste your UML diagram XML here..."
        ),
        gr.Textbox(
            label="User Input / Analysis Request",
            value=default_user_input,
            lines=3,
            placeholder="Enter your analysis request..."
        )
    ],
    outputs=gr.JSON(label="Analysis Result"),
    title="UML Class Diagram Analyzer",
    description="Analyze UML class diagrams for structural validity, relationship correctness, and design quality.",
    api_name="LLD"
)

if __name__ == "__main__":
    demo.launch()
