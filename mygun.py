# -*- coding: utf-8 -*-
"""
@name:creat the tem gun module

Created on Wed May 13 15:06:54 2020

@author: YangFan
"""

import execjs

def getguntilt():
        jsstr='''
            function getguntilt()
            {
                var myTEM= new ActiveXOject("TEMScripting.Instrument");
                var mygun=myTem.Gun;
                var myguntilt=mygun.Tilt;
                return(myguntilt.x,myguntilt.y);
            }
            '''
        js2py=execjs.compile(jsstr)
        return(js2py.call('getguntilt'))
def setguntilt(tiltx,tilty):
        jsstr='''
            function setguntilt(x,y)
            {
                var myTEM= new ActiveXOject("TEMScripting.Instrument");
                var mygun=myTem.Gun;
                mygun.Tilt.x=x;
                mygun.Tilt.y=y;
            }
            '''
        js2py=execjs.compile(jsstr)
        return(js2py.call('setguntilt',tiltx,tilty))
def getgunshift():
        jsstr='''
            function getgunshift()
            {
                var myTEM= new ActiveXOject("TEMScripting.Instrument");
                var mygun=myTem.Gun;
                var mygunshift=mygun.Shift;
                return(mygunshift.x,mygunshift.y);
            }
            '''
        js2py=execjs.compile(jsstr)
        return(js2py.call('getguntilt'))
def setgunshift(shiftx,shifty)
        jsstr='''
            function setgunshift(x,y)
            {
                var myTEM= new ActiveXOject("TEMScripting.Instrument");
                var mygun=myTem.Gun;
                mygun.Shift.x=x;
                mygun.Shift.y=y;
            }
            '''
        js2py=execjs.compile(jsstr)
        return(js2py.call('setgunshitf',shiftx,shifty))
def getHTstate():
        jsstr='''
            function getHTstate()
            {
                var myTEM= new ActiveXOject("TEMScripting.Instrument");
                var mygun=myTem.Gun;
                var mygunhtstate=mygun.HTState;
                return(mygunhtstate);
            }
            '''
        js2py=execjs.compile(jsstr)
        tmpa=js2py.call('getHTstate')
        result=""
        if int(tmpa)==0:
            result="High Tension is off "
        if int(tmpa)==1:
            result="High Tension is on"
        if int(tmpa)==2:
            result="High Tension is disabled"
        return(tmpa,result)
def setHTstate(x):
        jsstr='''
            function setHTstate(x)
            {
                var myTEM= new ActiveXOject("TEMScripting.Instrument");
                var mygun=myTem.Gun;
                mygun.HTState=x;
            }
            '''
        js2py=execjs.compile(jsstr)
        return(js2py.call('setHTstate',x))
def getHTvalue():
        jsstr='''
            function gethtvalue()
            {
                var myTEM= new ActiveXOject("TEMScripting.Instrument");
                var mygun=myTem.Gun;
                var mygunhtvalue=mygun.HTValue;
                return(mygunhtvalue);
            }
            '''
        js2py=execjs.compile(jsstr)
        return(js2py.call('gethtvalue'))
def setHTvalue(x):
        jsstr='''
            function setguntilt(x,y)
            {
                var myTEM= new ActiveXOject("TEMScripting.Instrument");
                var mygun=myTem.Gun;
                mygun.HTValue=x;
            }
            '''
        js2py=execjs.compile(jsstr)
        return(js2py.call('setHTvalue',x))
def getHTmaxvalue():
        jsstr='''
            function gethtmaxvalue()
            {
                var myTEM= new ActiveXOject("TEMScripting.Instrument");
                var mygun=myTem.Gun;
                var mygunhtmaxvalue=mygun.HTMaxValue;
                return(mygunhtmaxvalue);
            }
            '''
        js2py=execjs.compile(jsstr)
        return(js2py.call('gethtmaxvalue'))









