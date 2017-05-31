import datetime
import requests
import re
import xml.etree.ElementTree as ET
import time

def testme(event,context):
	date = datetime.datetime.now()-datetime.timedelta(days=1)
	alldays=[]
	for l in range(1):
		date += datetime.timedelta(days=1)
		onedate=re.sub(r'\s.*','',str(date))
		xml = """<?xml version="1.0" encoding="UTF-8"?>
		<p:DCTRequest xsi:schemaLocation="http://www.dhl.com DCT-req.xsd " xmlns:p="http://www.dhl.com" xmlns:p1="http://www.dhl.com/datatypes" xmlns:p2="http://www.dhl.com/DCTRequestdatatypes" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
		  <GetQuote>
		    <Request>
		      <ServiceHeader>
		  	    <SiteID>SRBFrance</SiteID> 
		  	    <Password>jXxlVhceKE</Password> 
		      </ServiceHeader>
		    </Request>
		    <From>
		      <CountryCode>FR</CountryCode>
		      <Postalcode>31100</Postalcode>
		      <City>TOULOUSE</City>
		    </From>
		    <BkgDetails>
		      <PaymentCountryCode>FR</PaymentCountryCode>
		      <Date>"""+onedate+"""</Date>
		      <ReadyTime>PT10H21M</ReadyTime>
		      <ReadyTimeGMTOffset>+01:00</ReadyTimeGMTOffset>
		      <DimensionUnit>CM</DimensionUnit>
		      <WeightUnit>KG</WeightUnit>
		      <Pieces>
		        <Piece>
		          <PieceID>1</PieceID>
		          <Height>1</Height>
		          <Depth>1</Depth>
		          <Width>1</Width>
		          <Weight>0.5</Weight>
		        </Piece>
		      </Pieces>
		      <PaymentAccountNumber>223932540</PaymentAccountNumber>      
		      <IsDutiable>N</IsDutiable>
		      <NetworkTypeCode>AL</NetworkTypeCode>
		    </BkgDetails>
		    <To>
		      <CountryCode>BE</CountryCode>
		      <Postalcode>1000</Postalcode>
			  <City>BRUSSELS</City>
		    </To>
		  </GetQuote>
		</p:DCTRequest>"""
		headers = {'Content-Type': 'application/xml'} # set what your server accepts
		resp=requests.post('https://xmlpitest-ea.dhl.com/XMLShippingServlet', data=xml, headers=headers).text
		print resp
		root = ET.fromstring(resp)
		allstartdate=[]
		
print testme("s","s")
# print getTest()