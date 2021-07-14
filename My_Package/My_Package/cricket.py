#Function For Batting

def bat(runs,balls,fours,six,field):
    strike_rate=(runs/balls)*100
    points=runs/2

    if (runs>=50):
        points=points+5
    if (runs>=100):
        points=points+10
    if (strike_rate>=80 and strike_rate<=100):
        points=points+2
    if (strike_rate>100):
        points=points+4
    if (fours>0):
        points=points+(fours*1)
    if (six>0):
        points=points+(six*2)
    if (field>0):
        points=points+(field*10)

    return(points)


#Function For Bowling

def bowl(wkts,runs,overs,field):
    points=wkts*10
    eco_rate=runs/overs

    if (wkts>2 and wkts<5):
        points=points+5
    if (wkts>=5):
        points=points+10
    if (eco_rate>=3.5 and eco_rate<=4.5):
        points=points+4
    if (eco_rate>=2 and eco_rate<3.5):
        points=points+7
    if (eco_rate<2):
        points=points+10
   

    return(points)

p1={'name':'Virat Kohli', 'role':'bat', 'runs':112, '4':10, '6':0,
'balls':119, 'field':0}
p2={'name':'du Plessis', 'role':'bat', 'runs':120, '4':11, '6':2,
'balls':112, 'field':0}
p3={'name':'Bhuvneshwar Kumar', 'role':'bowl', 'wkts':1, 'overs':10,
'runs':71, 'field':1}
p4={'name':'Yuzvendra Chahal', 'role':'bowl', 'wkts':2, 'overs':10,
'runs':45, 'field':0}
p5={'name':'Kuldeep Yadav', 'role':'bowl', 'wkts':3, 'overs':10, 'runs':34,
'field':0}

input_list=[p1,p2,p3,p4,p5]
output_list=[]
for p in input_list:
    if(p.get('role')=='bat'):
        points=bat(p.get('runs'),p.get('balls'),p.get('4'),p.get('6'),p.get('field'))
        output_list.append({'name': p.get('name'), 'batscore':points})
    else:
        if(p.get('role')=='bowl'):
            points=bowl(p.get('wkts'),p.get('runs'),p.get('overs'),p.get('field'))
            output_list.append({'name':p.get('name'), 'bowlscore':points})
for item in output_list:
    print(item)
            



        
