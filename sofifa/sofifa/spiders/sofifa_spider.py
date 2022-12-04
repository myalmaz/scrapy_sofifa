import scrapy
from ..items import SofifaItem

class QuotesSpider(scrapy.Spider):
    name = "sofifa"
    start_urls = ['https://sofifa.com/']

    def parse(self, response):
        players = response.xpath('//tbody[@class="list"]//tr//td[@class="col-name"]/a[1]/@href').getall()
        for i in players:
            yield response.follow(i, callback=self.parse_player)
        # next = response.xpath('//span[@class="bp3-button-text" and text()="Next"]/parent::a/@href').get()
        # yield from response.follow_all(next, self.parse)

    def parse_player(self, response):
        FIFA_crossing = int(response.xpath('//div[@class="card" and h5/text()="Attacking"]//ul//li[1]//span/text()').get())
        FIFA_finishing = int(response.xpath('//div[@class="card" and h5/text()="Attacking"]//ul//li[2]//span/text()').get())
        FIFA_heading_accuracy = int(response.xpath('//div[@class="card" and h5/text()="Attacking"]//ul//li[3]//span/text()').get())
        FIFA_short_passing = int(response.xpath('//div[@class="card" and h5/text()="Attacking"]//ul//li[4]//span/text()').get())
        FIFA_volleys = int(response.xpath('//div[@class="card" and h5/text()="Attacking"]//ul//li[5]//span/text()').get())
        # Defino todas las variables de la columna TECNICA
        FIFA_dribbling = int(response.xpath('//div[@class="card" and h5/text()="Skill"]//ul//li[1]//span/text()').get())
        FIFA_curve = int(response.xpath('//div[@class="card" and h5/text()="Skill"]//ul//li[2]//span/text()').get())
        FIFA_fk_accuracy = int(response.xpath('//div[@class="card" and h5/text()="Skill"]//ul//li[3]//span/text()').get())
        FIFA_long_passing = int(response.xpath('//div[@class="card" and h5/text()="Skill"]//ul//li[4]//span/text()').get())
        FIFA_ball_control = int(response.xpath('//div[@class="card" and h5/text()="Skill"]//ul//li[5]//span/text()').get())
        # Defino todas las variables de la columna MOVIMIENTO
        FIFA_acceleration = int(response.xpath('//div[@class="card" and h5/text()="Movement"]//ul//li[1]//span/text()').get())
        FIFA_sprint_speed = int(response.xpath('//div[@class="card" and h5/text()="Movement"]//ul//li[2]//span/text()').get())
        FIFA_agility = int(response.xpath('//div[@class="card" and h5/text()="Movement"]//ul//li[3]//span/text()').get())
        FIFA_reactions = int(response.xpath('//div[@class="card" and h5/text()="Movement"]//ul//li[4]//span/text()').get())
        FIFA_balance = int(response.xpath('//div[@class="card" and h5/text()="Movement"]//ul//li[5]//span/text()').get())
        # Defino todas las variables de la columna POTENCIA
        FIFA_shot_power = int(response.xpath('//div[@class="card" and h5/text()="Power"]//ul//li[1]//span/text()').get())
        FIFA_jumping = int(response.xpath('//div[@class="card" and h5/text()="Power"]//ul//li[2]//span/text()').get())
        FIFA_stamina = int(response.xpath('//div[@class="card" and h5/text()="Power"]//ul//li[3]//span/text()').get())
        FIFA_strength = int(response.xpath('//div[@class="card" and h5/text()="Power"]//ul//li[4]//span/text()').get())
        FIFA_long_shots = int(response.xpath('//div[@class="card" and h5/text()="Power"]//ul//li[5]//span/text()').get())
        # Defino todas las variables de la columna MENTALIDAD
        FIFA_aggression = int(response.xpath('//div[@class="card" and h5/text()="Mentality"]//ul//li[1]//span/text()').get())
        FIFA_interceptions = int(response.xpath('//div[@class="card" and h5/text()="Mentality"]//ul//li[2]//span/text()').get())
        FIFA_positioning = int(response.xpath('//div[@class="card" and h5/text()="Mentality"]//ul//li[3]//span/text()').get())
        FIFA_vision = int(response.xpath('//div[@class="card" and h5/text()="Mentality"]//ul//li[4]//span/text()').get())
        FIFA_penalties = int(response.xpath('//div[@class="card" and h5/text()="Mentality"]//ul//li[5]//span/text()').get())
        FIFA_composure = int(response.xpath('//div[@class="card" and h5/text()="Mentality"]//ul//li[6]//span/text()').get())
        # Defino todas las variables de la columna DEFENSA
        FIFA_defensive_awareness = int(response.xpath('//div[@class="card" and h5/text()="Defending"]//ul//li[1]//span/text()').get())
        FIFA_standing_tackle = int(response.xpath('//div[@class="card" and h5/text()="Defending"]//ul//li[2]//span/text()').get())
        FIFA_sliding_tackle = int(response.xpath('//div[@class="card" and h5/text()="Defending"]//ul//li[3]//span/text()').get())
        # Defino todas las variables de la columna PORTERO
        FIFA_GK_diving = int(response.xpath('//div[@class="card" and h5/text()="Goalkeeping"]//ul//li[1]//span/text()').get())
        FIFA_GK_handling = int(response.xpath('//div[@class="card" and h5/text()="Goalkeeping"]//ul//li[2]//span/text()').get())
        FIFA_GK_kicking = int(response.xpath('//div[@class="card" and h5/text()="Goalkeeping"]//ul//li[3]//span/text()').get())
        FIFA_GK_positioning = int(response.xpath('//div[@class="card" and h5/text()="Goalkeeping"]//ul//li[4]//span/text()').get())
        FIFA_GK_reflexes = int(response.xpath('//div[@class="card" and h5/text()="Goalkeeping"]//ul//li[5]//span/text()').get())
        traits = response.xpath('//div[@class="card" and h5/text()="Traits"]//ul//li//span/text()').getall()
        try:
            s_h2 = []
        except:
            s_h2 = response.xpath('//div[@class="card" and h5/text()="Player Specialities"]//ul//li//a/text()').getall()
        s_h = []
        for i in s_h:
            i.replace('#','')
            s_h.append(i)

        #profile
        foot = response.xpath('//div[@class="card" and h5/text()="Profile"]//ul//li[1]/text()').get()
        name = response.xpath('//div[@class="info"]//h1/text()').get()
        Position = response.xpath('//div[@class="meta ellipsis"]//span/text()').getall()
        Best_Position = response.xpath('//div[@class="center"]//li[@class="ellipsis"][1]//span/text()').get()
        Overall_Rating = int(response.xpath('//section[@class="card spacing"]//div[@class="block-quarter"][1]//span/text()').get())
        Potential_Rating = int(response.xpath('//section[@class="card spacing"]//div[@class="block-quarter"][2]//span/text()').get())


        item = SofifaItem()

        item['Name'] = name
        item['Positions'] = Position
        item['Registred_Positions'] = Best_Position
        item['Rating'] = Overall_Rating
        item['Potential_Rating'] = Potential_Rating
        item['Injury_Tolerance'] = 'B'
        if 'Solid Player' in traits:
            item['Injury_Tolerance'] = 'A'
        elif 'Injury Prone' in traits:
            item['Injury_Tolerance'] = 'C'
        item['Foot'] = foot
        item['Attack'] = int(round((int(FIFA_finishing) + int(FIFA_dribbling) + int(FIFA_positioning))/3)) - 5
        if 'Complete Forward' in traits:
            item['Attack'] += 5
        if 'Poacher' in s_h:
            item['Attack'] += 2
        if 'Aerial Threat' in s_h:
            item['Attack'] += 2
        if 'Finesse Shot' in traits:
            item['Attack'] += 2
        if 'Clinical Finisher' in s_h:
            item['Attack'] += 2
        if Best_Position == 'GK':
            PES5_Attack = 30
        item['Defence'] = FIFA_defensive_awareness
        if Best_Position == 'GK':
            item['Defence'] = FIFA_GK_positioning
        item['Balance'] = FIFA_strength
        item['Stamina'] = FIFA_stamina
        if Best_Position == 'GK':
            item['Stamina'] += 45
        item['Speed'] = FIFA_sprint_speed
        item['Acceleration'] = FIFA_acceleration
        item['Response'] = FIFA_reactions
        if Best_Position == 'GK':
            item['Response'] = FIFA_GK_reflexes
        item['Agility'] = FIFA_agility
        if Best_Position == 'GK':
            item['Agility'] = FIFA_GK_diving
        item['Dribble_Accuracy'] = FIFA_dribbling
        item['Dribble_Speed'] = int(round(int(FIFA_dribbling)/3) + round(int(FIFA_agility)/3) + round(int(FIFA_ball_control) /3))
        item['Short_Pass_Accuracy'] = FIFA_short_passing
        item['Short_Pass_Speed'] = FIFA_vision
        item['Long_Pass_Accuracy'] = FIFA_long_passing
        item['Long_Pass_Speed'] = int(round(int(FIFA_crossing)/2) + round(int(FIFA_vision)/2))
        item['Shot_Accuracy'] = FIFA_finishing
        item['Shot_Power'] = FIFA_shot_power
        item['Shot_Technique'] = int(round(int(FIFA_finishing)/3)+ round(int(FIFA_ball_control)/3) + round(int(FIFA_volleys)/3))
        item['Free_Kick_Accuracy'] = FIFA_fk_accuracy
        item['Swerve'] = FIFA_curve
        item['Heading'] = FIFA_heading_accuracy
        item['Jump'] = FIFA_jumping
        item['Technique'] = FIFA_ball_control
        if Best_Position == 'GK':
            item['Aggression'] = 50 + int((int(FIFA_finishing) + int(item['Attack']))/12)
        if Best_Position == 'CB':
            item['Aggression'] = 50 + int((int(FIFA_finishing) + int(item['Attack'])) / 12)
        if Best_Position == 'LB' or Best_Position == 'RB':
            item['Aggression'] = 55 + int((int(FIFA_finishing) + int(item['Attack']))/12)
        if Best_Position == 'CDM':
            item['Aggression'] = 67 + int((int(FIFA_finishing) + int(item['Attack']))/12)
        if Best_Position == 'LWB' or Best_Position == 'RWB':
            item['Aggression'] = 60 + int((int(FIFA_finishing) + int(item['Attack']))/12)
        if Best_Position == 'CM':
            item['Aggression'] = 70 + int((int(FIFA_finishing) + int(item['Attack']))/12)
        if Best_Position == 'LM' or Best_Position == 'RM':
            item['Aggression'] = 67 + int((int(FIFA_finishing) + int(item['Attack']))/12)
        if Best_Position == 'CAM':
            item['Aggression'] = 70 + int((int(FIFA_finishing) + item['Attack'])/12)
        if Best_Position == 'LW' or Best_Position == 'RW':
            item['Aggression'] = 75 + int((int(FIFA_finishing) + item['Attack'])/12)
        else:
            item['Aggression'] = 80 + int((int(FIFA_finishing) + item['Attack'])/12)
        item['Mentality'] = FIFA_composure
        if Best_Position == 'GK':
            item['Mentality'] = int(int(FIFA_composure)/2) + 50
        item['GK_Skills'] = int(round((int(FIFA_GK_handling) + int(FIFA_GK_diving) + int(FIFA_GK_reflexes) + int(FIFA_GK_positioning))/4))
        item['Team_work'] = FIFA_positioning
        item['Condition_Fitness'] = int(round(int(FIFA_stamina)/12.5))
        if 'Dribbler' in s_h:
            item['Spec_Dribbling'] = 1
        if ' Speed Dribbler (AI)' in traits:
            item['Spec_Tactical_Dribble'] = 1
        if int(FIFA_positioning) > 75:
            item['Spec_Positioning'] = 1
        if int(FIFA_reactions) > 79:
            item['Spec_Reaction'] = 1
        if 'Playmaker' in s_h:
            item['Spec_Playmaking'] = 1
        if int(FIFA_short_passing) > 79:
            item['Spec_Passing'] = 1
        if 'Clinical Finisher' in s_h:
            item['Spec_Scoring'] = 1
        if int(FIFA_finishing) > 79:
            item['Spec_1_1_Scoring'] = 1
        if Best_Position == 'ST' and 'Strength' in s_h:
            item['Spec_Post_Player'] = 1
        if 'Complete Forward' in s_h or 'Complete Defender' in s_h:
            item['Spec_Lines'] = 1
        if 'Distance Shooter' in s_h or 'Long Shot Taker (AI)' in traits:
            item['Spec_Middle_Shooting'] = 1
        if int(FIFA_penalties) >= 79:
            item['Spec_Penalties'] = 1
        if int(FIFA_volleys) > 79:
            item['Spec_1_Touch_Pass'] = 1
        if 'Outside Foot Shot' in traits:
            item['Spec_Outside'] = 1
        if int(FIFA_defensive_awareness) > 79:
            item['Spec_Marking'] = 1
        if 'Tackling' in s_h:
            item['Spec_Sliding'] = 1
        if 'Tactician' in s_h:
            item['Spec_Covering'] = 1
        if 'Complete Defender' in s_h:
            item['Spec_D_Line_Control'] = 1
        if int(FIFA_GK_reflexes) > 79:
            item['Spec_Penalty_Stopper'] = 1
        if int(FIFA_GK_positioning) > 79:
            item['Spec_1_On_1_Stopper'] = 1
        if 'Long Throw-in' in traits:
            item['Spec_Long_Throw'] = 1

        item['Injury_Tolerance'] = 'B'
        if 'Solid Player' in traits:
            item['Injury_Tolerance'] = 'A'
        elif 'Injury Prone' in traits:
            item['Injury_Tolerance'] = 'C'


        yield item