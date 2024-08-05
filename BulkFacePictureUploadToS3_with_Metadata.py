import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('1.jpg','APJ Kalam'),
      ('2.jpg','CV Raman'),
      ('3.jpg','David Bekhm'),
      ('4.png','Albert Einstein'),
      ('5.jpg','Isaac Newton'),
      ('6.png','Lionel Messi'),
      ('7.jpeg','Nikola Tesla'),
      ('8.jpeg','Mahendra Singh Dhoni'),
      ('9.jpeg','Mithali Raj'),
      ('10.jpeg','Smriti Mandhana'),
      ('11.jpeg','Hardik Pandya'),
      ('12.jpeg','Yuvraj Singh'),
      ('13.jpg','Sachin Tendulkar'),
      ('14.jpeg','Yuzvendra Chahal'),
      ('15.jpeg','Virat Kohli'),
      ('16.jpg','Sunil Gavaskar'),
      ('17.jpg','Kapil Dev'),
      ('18.jpeg','Ruturaj Gaikwad'),
      ('19.jpeg','Kiran Kumar Malik'),
      ('20.jpeg','Sagar Kumar Ojha'),
      ('21.jpeg','Sarukh Khan'),
      ('22.jpg','Harleen Deol'),
      ('23.png','Chandan Kumar Sahu')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('facialsimagescollections','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]}
                    )