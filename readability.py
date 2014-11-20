from textstat.textstat import textstat as ts

def ascii(s):
  return s.encode('ascii', 'ignore')

article = """
A spokesman for House Speaker John Boehner (R-Ohio) labeled President Barack Obama as “Emperor Obama” on Wednesday, after the White House leaked to reporters that the president would act unilaterally on Friday to amend U.S. immigration laws.

“If ‘Emperor Obama’ ignores the American people and announces an amnesty plan that he himself has said over and over again exceeds his constitutional authority, he will cement his legacy of lawlessness and ruin the chances for congressional action on this issue – and many others,” Boehner spokesman Michael Steel said.

President Barack Obama walks towards a group of supporters after arriving at San Francisco International airport, on Friday, Oct. 10, 2014, in San Francisco. Obama is visiting San Francisco for fundraiser events. (AP Photo/Evan Vucci) AP Photo/Evan Vucci
President Barack Obama is set to announce his unilateral action on immigration on Friday in Las Vegas, while Republicans say doing so would ‘cement his legacy of lawlessness.’ (AP Photo/Evan Vucci)
It was widely reported Wednesday morning that Obama would announce his long-awaited and hotly contested executive amnesty on immigration on Friday, during a visit to Las Vegas. That plan is expected to create legal status for millions of illegal immigrants, and allow them to work.

According to the Wall Street Journal, the plan is expected to expand the deferred action program that has already given protected status to 600,000 younger illegal immigrants. It might also protect parents and spouses of U.S. citizens who are in the country illegally.

For the last few weeks, Obama has been expected to loosen the rules regarding green cards, so that, for example, family members would be seen as legal residents even if just one parent actually holds a green card.

Republicans have continued to criticize Obama’s move as one that would go around Congress to rewrite immigration laws. The GOP has also said that Obama himself has said several times that he is not permitted to take certain actions without Congress.

Boehner’s staff on Wednesday released a list of 22 times that Obama has said the president has limited powers, and can’t act on his own.

“You don’t want a president who’s too powerful or a Congress that’s too powerful or a court that’s too powerful,” Obama said in 2008. “Everybody’s got their own role.”




"""

ts.flesch_reading_ease(article)
