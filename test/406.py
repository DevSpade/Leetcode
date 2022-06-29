        # 제일 작은 숫자로 위치 세팅 가능
        # 그 다음 작은 사람도 위치 세팅 가능
        # 뒤에가 0인 인자 중에 가장 작은 숫자가 제일 앞
        
        sortedPeople = sorted(people)
        dictPeople = {}

        # 사이즈 만큼 dict 생성
        for i in range(0, len(sortedPeople)) :
            dictPeople.setdefault(i)

        for people in sortedPeople :
            if dictPeople[people[1]] != None :
                if dictPeople[people[1]] <              
            else :
                dictPeople[people[1]] = people
            
        #print(dictPeople)
            
        
        # 제일 작은것 세팅
        
        # 그 다음 작은 것
        
        
        #print(sortedPeople)
        
        #        dictPeople 
        
        
        
        return None
        