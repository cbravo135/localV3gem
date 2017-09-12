from rw_reg import *

ohN = 0
vfatN = 3
vfatRegPath = 'GEM_AMC.OH.OH%i.GEB.VFAT%i'%(ohN,vfatN)

scanDAC = 'CAL_DAC'
monDAC = 33

dacSize = 256

#Initialize system
parseXML()

print 'Configuring VFAT'
writeReg(getNode(vfatRegPath+'.CFG_IREF'),22)
writeReg(getNode(vfatRegPath+'.CFG_VREF_ADC'),3)
writeReg(getNode(vfatRegPath+'.CFG_MONITOR_SELECT'),monDAC)
writeReg(getNode(vfatRegPath+'.CFG_RUN'),1)

writeReg(getNode(vfatRegPath+'.CFG_CAL_SEL_POL'),0)

print 'Start Scan'
outF = open('/mnt/persistent/texas/data/testData.txt','w')
outF.write('dacVal/I:ADC0/I\n')
for dacVal in range(dacSize):
    writeReg(getNode(vfatRegPath+'.CFG_'+scanDAC),dacVal)
    adcVal = readReg(getNode(vfatRegPath+'.ADC0'))
    outF.write('%i\t%i\n'%(dacVal,int(adcVal,0)))
    pass
outF.close()
