#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime


from lldproj.crew import LLDProjectCrew
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

diagram = """
<diagram>
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
</diagram>
"""
user_input = "Please analyze the following UML class diagram and provide a detailed report on the structural validity, relationship correctness, and design quality of the classes and relationships."

def run():
    inputs = {
        "diagram_input": diagram,
        "user_input": user_input,      # Raw diagram JSON/XML or parsed intermediate representation

    }
    result = LLDProjectCrew().crew().kickoff(inputs=inputs)
    print("\n\n===Final Result===\n\n", result.raw)

if __name__ == "__main__":
    run()