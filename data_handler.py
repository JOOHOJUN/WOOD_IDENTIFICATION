import pandas
import data_
import random

class data_handler():

    def __init__(self):
        self.loading_data(data_.data_list)
    def loading_data(self,data_list):
        self.Gua =list()
        self.sokk =list()
        self.content =list()
        for data in data_list:
            self.Gua = self.Gua+[data[i][0] for i in range(len(data))]
            self.sokk = self.sokk+[data[i][1] for i in range(len(data))]
            self.content = self.content +[data[i][2] for i in range(len(data))]
            self.list_len=len(self.Gua)
            self.random_list = random.sample(range(self.list_len), self.list_len)

    def reset_random_list(self):
        self.random_list = random.sample(range(self.list_len), self.list_len)

    def get_random(self, number):
        if self.list_len <= number:
            return -1
        else:
            return self.random_list[number]

    def get_result(self,number):
        num = self.get_random(number)
        result = self.sokk[num].strip()+' - '+self.Gua[num].strip()
        return result

    def get_content(self,number):
        num = self.get_random(number)
        if num== -1 :
            self.reset_random_list()
            return '끝입니다.'
        num_content = self.content[num]
        #문자 설정
        split_content = num_content.split(',')
        rd_num =random.sample(range(len(split_content)),len(split_content))
        content_data =str()
        for i,rd in enumerate(rd_num):
            content_data= content_data+str(i+1)+' '+split_content[rd].strip()+'\n'
        return content_data

a = data_handler()
a.get_result(1)