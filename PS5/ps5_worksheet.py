# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:49:39 2019

@author: alexk
"""


#Old solution to problem 2
   # Set up text to be searched by replacing puncuation with spaces and then splitting at spaces
#        split_text = text.lower()
#        for p in string.punctuation:
#            split_text = split_text.replace(p, ' ')
#        split_text = split_text.split(' ')
#        
#        # Need to split the phrase so we can compare words in split text with words in phrase
#        split_phrase = self.phrase.split(' ')
#        
#        #Loops to check whether the phrase is found in consecutive terms in text
#        # Going to loop over each term in split text
#        for i in range(len(split_text)):
#            # if a term in split text matches the first word in the phrase
#            if split_text[i] == split_phrase[0]:
#                #Then, start another loop the length of the phrase
#                for j in range(len(split_phrase)):
#                    # Then, if the succeeding terms of split text don't match phrase break the loop
#                    if split_phrase[j] != split_text[i + j]:
#                        break
#                # If managed to go through every term in phrase without breaking then the whole phrase
#                #has been found in consecutive terms in the text and we can return True
#                return True
#        #If reach this point, then the whole phrase WASN'T found and we return False
#        return False
   
   # Problem 5
#from datetime import datetime
#import pytz
##
#Birthday = '8 Jan 1995 9:35:20'
#dt_bday = datetime.strptime(Birthday, '%d %b %Y %H:%M:%S').replace(tzinfo = pytz.timezone('US/Eastern'))
#print (dt_bday)
#
##dt_now = datetime.datetime.now(tz = pytz.timezone('US/Eastern'))
##print(dt_now)
##
##
#
#daydelta = datetime.timedelta(days=1)
#tmrw = datetime.datetime.now() + daydelta
#print (tmrw)
#
#tmrw_str = datetime.datetime
#
#
#Problem 11
#
#def read_trigger_config(filename):
#    """
#    filename: the name of a trigger configuration file
#
#    Returns: a list of trigger objects specified by the trigger configuration
#        file.
#    """
#    # We give you the code to read in the file and eliminate blank lines and
#    # comments. You don't need to know how it works for now!
#    trigger_file = open(filename, 'r')
#    lines = []
#    for line in trigger_file:
#        line = line.rstrip()
#        if not (len(line) == 0 or line.startswith('//')):
#            lines.append(line)
#    
#    trigger_dict = create_trigger_dict(lines)
#    triggerlist = []
#    
#    def create_trigger(trigger_name):
#        trigger_info = trigger_dict[trigger_name]
#        
#        if trigger_info[0] == 'DESCRIPTION':
#            trigger_name = DescriptionTrigger(trigger_info[1])
#        
#        if trigger_info[0] == 'TITLE':
#            trigger_name == TitleTrigger(trigger_info[1])
#            
#        if trigger_info[0] == 'BEFORE':
#            trigger_name == BeforeTrigger(trigger_info[1])
#    
#        if trigger_info[0] == 'AFTER':
#            trigger_name == AfterTrigger(trigger_info[1])
#                      
#        if trigger_info[0] == 'AND':
#            trigger_name == AndTrigger(trigger_info[1], trigger_info[2])
#    
#        if trigger_info[0] == 'OR':
#            trigger_name == OrTrigger(trigger_info[1], trigger_info[2])
#       
#        if trigger_info[0] == 'NOT':
#            trigger_name == NotTrigger(trigger_info[1])  
#        
#        return trigger_name
#
#    for line in lines:
#        if line.startswith('ADD'):
#            split_line = line.split(',')
#            for trigger_name in split_line[1:]:
#                triggerlist.append(create_trigger(trigger_name))
#    
            
            
#Helper function for read trigger config.
#def create_trigger_dict(text_list):
#    trigger_dict = {}
#    for line in text_list:
#        if not line.startswith('ADD'):
#            trigger_info = line.split(',')
#            trigger_dict[trigger_info[0]] = trigger_info[1:]
#    return trigger_dict
#    