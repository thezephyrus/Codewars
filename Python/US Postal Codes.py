'''
Given the name of a US state or territory, return its postal abbreviation. All states, federal districts and inhibited territories will be tested, according to the linked wikipedia page.

Notes:

to spark your creativity, the size of your code is limited to 500 characters
the list of states and their respective abbreviations are listed below
import, exec, eval and "__" are forbidden
Examples
"Alabama"               -->  "AL"
"District of Columbia"  -->  "DC"
"U.S. Virgin Islands"   -->  "VI"


List of states and abbreviations
--------------------------------
Alabama, AL
Alaska, AK
Arizona, AZ
Arkansas, AR
California, CA
Colorado, CO
Connecticut, CT
Delaware, DE
Florida, FL
Georgia, GA
Hawaii, HI
Idaho, ID
Illinois, IL
Indiana, IN
Iowa, IA
Kansas, KS
Kentucky, KY
Louisiana, LA
Maine, ME
Maryland, MD
Massachusetts, MA
Michigan, MI
Minnesota, MN
Mississippi, MS
Missouri, MO
Montana, MT
Nebraska, NE
Nevada, NV
New Hampshire, NH
New Jersey, NJ
New Mexico, NM
New York, NY
North Carolina, NC
North Dakota, ND
Ohio, OH
Oklahoma, OK
Oregon, OR
Pennsylvania, PA
Rhode Island, RI
South Carolina, SC
South Dakota, SD
Tennessee, TN
Texas, TX
Utah, UT
Vermont, VT
Virginia, VA
Washington, WA
West Virginia, WV
Wisconsin, WI
Wyoming, WY
District of Columbia, DC
American Samoa, AS
Guam, GU
Northern Mariana Islands, MP
Puerto Rico, PR
U.S. Virgin Islands, VI

'''
def abbr(s):
    if 'U.' in s: return 'VI'
    if 'Mari' in s:return 'MP'
    if ' ' in s: return "".join(w[0] for w in s.replace(' of ', ' ').split()).upper()
    c = dict(Alab='AL', Alas='AK', Ariz='AZ', Conn='CT', Geor='GA', Hawa='HI', Iowa='IA', Kans='KS', Kent='KY', Loui='LA', Main='ME', Mary='MD', Minn='MN', Missi='MS', Misso='MO', Mont='MT', Neva='NV', Penn='PA', Tenn='TN', Texa='TX', Verm='VT', Virg='VA', Nort='MP')
    return c.get(s[:4], c.get(s[:5], s[:2].upper()))