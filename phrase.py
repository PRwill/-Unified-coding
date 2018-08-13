# -*- coding: gb2312 -*-
import os
import chardet
import sys

all_file = []
unicode_value = [u'\u4e00', u'\u4e01', u'\u4e03', u'\u4e07', u'\u4e08', u'\u4e09', u'\u4e09', u'\u4e0a',
                 u'\u4e0b', u'\u4e0d', u'\u4e0e', u'\u4e10', u'\u4e11', u'\u4e13', u'\u4e14', u'\u4e16',
                 u'\u4e18', u'\u4e19', u'\u4e1a', u'\u4e1b', u'\u4e1c', u'\u4e1d', u'\u4e22', u'\u4e24',
                 u'\u4e25', u'\u4e27', u'\u4e2a', u'\u4e2d', u'\u4e30', u'\u4e32', u'\u4e34', u'\u4e38',
                 u'\u4e39', u'\u4e3a', u'\u4e3b', u'\u4e3d', u'\u4e3e', u'\u4e43', u'\u4e45', u'\u4e48',
                 u'\u4e49', u'\u4e4b', u'\u4e4c', u'\u4e4d', u'\u4e4e', u'\u4e4f', u'\u4e50', u'\u4e52',
                 u'\u4e53', u'\u4e54', u'\u4e56', u'\u4e58', u'\u4e59', u'\u4e5d', u'\u4e5e', u'\u4e5f',
                 u'\u4e60', u'\u4e61', u'\u4e66', u'\u4e70', u'\u4e71', u'\u4e73', u'\u4e86', u'\u4e88',
                 u'\u4e89', u'\u4e8b', u'\u4e8c', u'\u4e8e', u'\u4e8f', u'\u4e91', u'\u4e92', u'\u4e94',
                 u'\u4e95', u'\u4e9a', u'\u4e9b', u'\u4ea1', u'\u4ea4', u'\u4ea5', u'\u4ea6', u'\u4ea7',
                 u'\u4ea9', u'\u4eab', u'\u4eac', u'\u4ead', u'\u4eae', u'\u4eb2', u'\u4eba', u'\u4ebf',
                 u'\u4ec0', u'\u4ec1', u'\u4ec5', u'\u4ec6', u'\u4ec7', u'\u4eca', u'\u4ecb', u'\u4ecd',
                 u'\u4ece', u'\u4ed1', u'\u4ed3', u'\u4ed4', u'\u4ed6', u'\u4ed7', u'\u4ed8', u'\u4ed9',
                 u'\u4ee3', u'\u4ee4', u'\u4ee5', u'\u4eea', u'\u4eec', u'\u4ef0', u'\u4ef2', u'\u4ef6',
                 u'\u4ef7', u'\u4efb', u'\u4efd', u'\u4eff', u'\u4f01', u'\u4f0a', u'\u4f0d', u'\u4f0f',
                 u'\u4f10', u'\u4f11', u'\u4f17', u'\u4f18', u'\u4f19', u'\u4f1a', u'\u4f1e', u'\u4f1f',
                 u'\u4f20', u'\u4f24', u'\u4f26', u'\u4f2a', u'\u4f2f', u'\u4f30', u'\u4f34', u'\u4f36',
                 u'\u4f38', u'\u4f3a', u'\u4f3c', u'\u4f43', u'\u4f46', u'\u4f4d', u'\u4f4e', u'\u4f4f',
                 u'\u4f51', u'\u4f53', u'\u4f55', u'\u4f59', u'\u4f5b', u'\u4f5c', u'\u4f60', u'\u4f63',
                 u'\u4f69', u'\u4f73', u'\u4f7f', u'\u4f84', u'\u4f88', u'\u4f8b', u'\u4f8d', u'\u4f9b',
                 u'\u4f9d', u'\u4fa0', u'\u4fa3', u'\u4fa5', u'\u4fa6', u'\u4fa7', u'\u4fa8', u'\u4fae',
                 u'\u4faf', u'\u4fb5', u'\u4fbf', u'\u4fc3', u'\u4fc4', u'\u4fca', u'\u4fcf', u'\u4fd0',
                 u'\u4fd7', u'\u4fd8', u'\u4fdd', u'\u4fe1', u'\u4fe9', u'\u4fed', u'\u4fee', u'\u4fef',
                 u'\u4ff1', u'\u4ffa', u'\u500d', u'\u5012', u'\u5014', u'\u5018', u'\u5019', u'\u501a',
                 u'\u501f', u'\u5021', u'\u5026', u'\u503a', u'\u503c', u'\u503e', u'\u5047', u'\u504e',
                 u'\u504f', u'\u505a', u'\u505c', u'\u5065', u'\u5076', u'\u5077', u'\u507f', u'\u5080',
                 u'\u5085', u'\u508d', u'\u50a8', u'\u50ac', u'\u50b2', u'\u50bb', u'\u50cf', u'\u50da',
                 u'\u50e7', u'\u50f5', u'\u50fb', u'\u5112', u'\u5121', u'\u513f', u'\u5141', u'\u5143',
                 u'\u5144', u'\u5145', u'\u5146', u'\u5148', u'\u5149', u'\u514b', u'\u514d', u'\u5151',
                 u'\u5154', u'\u515a', u'\u515c', u'\u5162', u'\u5165', u'\u5168', u'\u516b', u'\u516c',
                 u'\u516d', u'\u5170', u'\u5171', u'\u5173', u'\u5174', u'\u5175', u'\u5176', u'\u5177',
                 u'\u5178', u'\u517b', u'\u517c', u'\u517d', u'\u5180', u'\u5185', u'\u5188', u'\u518c',
                 u'\u518d', u'\u5192', u'\u5195', u'\u5197', u'\u5199', u'\u519b', u'\u519c', u'\u51a0',
                 u'\u51a4', u'\u51ac', u'\u51af', u'\u51b0', u'\u51b2', u'\u51b3', u'\u51b5', u'\u51b6',
                 u'\u51b7', u'\u51bb', u'\u51c0', u'\u51c4', u'\u51c6', u'\u51c9', u'\u51cc', u'\u51cf',
                 u'\u51d1', u'\u51db', u'\u51dd', u'\u51e0', u'\u51e1', u'\u51e4', u'\u51eb', u'\u51ed',
                 u'\u51ef', u'\u51f0', u'\u51f3', u'\u51f6', u'\u51f8', u'\u51f9', u'\u51fa', u'\u51fb',
                 u'\u51fd', u'\u51ff', u'\u5200', u'\u5201', u'\u5203', u'\u5206', u'\u5207', u'\u520a',
                 u'\u5211', u'\u5212', u'\u5217', u'\u5218', u'\u5219', u'\u521a', u'\u521b', u'\u521d',
                 u'\u5220', u'\u5224', u'\u5228', u'\u5229', u'\u522b', u'\u522e', u'\u5230', u'\u5236',
                 u'\u5237', u'\u5238', u'\u5239', u'\u523a', u'\u523b', u'\u523d', u'\u5242', u'\u5243',
                 u'\u524a', u'\u524d', u'\u5251', u'\u5254', u'\u5256', u'\u5265', u'\u5267', u'\u5269',
                 u'\u526a', u'\u526f', u'\u5272', u'\u527f', u'\u5288', u'\u529b', u'\u529d', u'\u529e',
                 u'\u529f', u'\u52a0', u'\u52a1', u'\u52a3', u'\u52a8', u'\u52a9', u'\u52aa', u'\u52ab',
                 u'\u52b1', u'\u52b2', u'\u52b3', u'\u52bf', u'\u52c3', u'\u52c7', u'\u52c9', u'\u52cb',
                 u'\u52d2', u'\u52d8', u'\u52df', u'\u52e4', u'\u52fa', u'\u52fe', u'\u52ff', u'\u5300',
                 u'\u5305', u'\u5306', u'\u5308', u'\u5315', u'\u5316', u'\u5317', u'\u5319', u'\u5320',
                 u'\u5323', u'\u532a', u'\u5339', u'\u533a', u'\u533b', u'\u533e', u'\u533f', u'\u5341',
                 u'\u5343', u'\u5347', u'\u5348', u'\u534a', u'\u534e', u'\u534f', u'\u5351', u'\u5352',
                 u'\u5353', u'\u5355', u'\u5356', u'\u5357', u'\u535a', u'\u535c', u'\u5360', u'\u5361',
                 u'\u5362', u'\u5364', u'\u5366', u'\u5367', u'\u536b', u'\u5370', u'\u5371', u'\u5373',
                 u'\u5374', u'\u5375', u'\u5377', u'\u5378', u'\u537f', u'\u5382', u'\u5385', u'\u5386',
                 u'\u5389', u'\u538b', u'\u538c', u'\u5395', u'\u5398', u'\u539a', u'\u539f', u'\u53a2',
                 u'\u53a6', u'\u53a8', u'\u53bb', u'\u53bf', u'\u53c2', u'\u53c8', u'\u53c9', u'\u53ca',
                 u'\u53cb', u'\u53cc', u'\u53cd', u'\u53d1', u'\u53d4', u'\u53d6', u'\u53d7', u'\u53d8',
                 u'\u53d9', u'\u53db', u'\u53e0', u'\u53e3', u'\u53e4', u'\u53e5', u'\u53e6', u'\u53e8',
                 u'\u53ea', u'\u53eb', u'\u53ec', u'\u53ed', u'\u53ee', u'\u53ef', u'\u53f0', u'\u53f2',
                 u'\u53f3', u'\u53f6', u'\u53f7', u'\u53f8', u'\u53f9', u'\u53fc', u'\u53fd', u'\u5401',
                 u'\u5403', u'\u5404', u'\u5406', u'\u5408', u'\u5409', u'\u540a', u'\u540c', u'\u540d',
                 u'\u540e', u'\u540f', u'\u5410', u'\u5411', u'\u5413', u'\u5415', u'\u5417', u'\u541b',
                 u'\u541d', u'\u541e', u'\u541f', u'\u5420', u'\u5426', u'\u5427', u'\u5428', u'\u5429',
                 u'\u542b', u'\u542c', u'\u542d', u'\u542e', u'\u542f', u'\u5431', u'\u5434', u'\u5435',
                 u'\u5438', u'\u5439', u'\u543b', u'\u543c', u'\u5440', u'\u5446', u'\u5448', u'\u544a',
                 u'\u5450', u'\u5455', u'\u5458', u'\u545b', u'\u545c', u'\u5462', u'\u5468', u'\u5473',
                 u'\u5475', u'\u547b', u'\u547c', u'\u547d', u'\u5486', u'\u548c', u'\u548f', u'\u5490',
                 u'\u5492', u'\u5495', u'\u5496', u'\u5499', u'\u54a7', u'\u54a8', u'\u54aa', u'\u54ac',
                 u'\u54b1', u'\u54b3', u'\u54b8', u'\u54bd', u'\u54c0', u'\u54c1', u'\u54c4', u'\u54c6',
                 u'\u54c8', u'\u54cd', u'\u54ce', u'\u54d1', u'\u54d7', u'\u54df', u'\u54e5', u'\u54e8',
                 u'\u54e9', u'\u54ea', u'\u54ed', u'\u54ee', u'\u54f2', u'\u54fa', u'\u54fc', u'\u5501',
                 u'\u5506', u'\u5507', u'\u5509', u'\u5510', u'\u5520', u'\u5524', u'\u5527', u'\u552c',
                 u'\u552e', u'\u552f', u'\u5531', u'\u553e', u'\u5543', u'\u5544', u'\u5546', u'\u554a',
                 u'\u5561', u'\u5564', u'\u5565', u'\u5566', u'\u5570', u'\u5578', u'\u557c', u'\u5582',
                 u'\u5584', u'\u5587', u'\u5589', u'\u558a', u'\u5598', u'\u559c', u'\u559d', u'\u55a7',
                 u'\u55b3', u'\u55b7', u'\u55bb', u'\u55c5', u'\u55d3', u'\u55dc', u'\u55e1', u'\u55e4',
                 u'\u55e6', u'\u55fd', u'\u5600', u'\u5601', u'\u5609', u'\u5631', u'\u5632', u'\u5634',
                 u'\u5636', u'\u5639', u'\u563f', u'\u5668', u'\u5669', u'\u566a', u'\u568e', u'\u56a3',
                 u'\u56b7', u'\u56bc', u'\u56ca', u'\u56da', u'\u56db', u'\u56de', u'\u56e0', u'\u56e2',
                 u'\u56e4', u'\u56ed', u'\u56f0', u'\u56f1', u'\u56f4', u'\u56fa', u'\u56fd', u'\u56fe',
                 u'\u5703', u'\u5706', u'\u5708', u'\u571f', u'\u5723', u'\u5728', u'\u5730', u'\u573a',
                 u'\u573e', u'\u5740', u'\u5747', u'\u574a', u'\u574e', u'\u574f', u'\u5750', u'\u5751',
                 u'\u5757', u'\u575a', u'\u575b', u'\u575d', u'\u575e', u'\u575f', u'\u5760', u'\u5761',
                 u'\u5764', u'\u5766', u'\u576a', u'\u576f', u'\u5777', u'\u5782', u'\u5783', u'\u5784',
                 u'\u578b', u'\u5792', u'\u579b', u'\u57a2', u'\u57a6', u'\u57ab', u'\u57ae', u'\u57c2',
                 u'\u57c3', u'\u57cb', u'\u57ce', u'\u57df', u'\u57e0', u'\u57f9', u'\u57fa', u'\u5802',
                 u'\u5806', u'\u5815', u'\u5821', u'\u5824', u'\u582a', u'\u5830', u'\u5835', u'\u584c',
                 u'\u5851', u'\u5854', u'\u5858', u'\u585e', u'\u586b', u'\u5883', u'\u5885', u'\u5893',
                 u'\u5899', u'\u589e', u'\u58a8', u'\u58a9', u'\u58c1', u'\u58d5', u'\u58e4', u'\u58eb',
                 u'\u58ee', u'\u58f0', u'\u58f3', u'\u58f6', u'\u58f9', u'\u5904', u'\u5907', u'\u590d',
                 u'\u590f', u'\u5915', u'\u5916', u'\u591a', u'\u591c', u'\u591f', u'\u5927', u'\u5929',
                 u'\u592a', u'\u592b', u'\u592d', u'\u592e', u'\u592f', u'\u5931', u'\u5934', u'\u5937',
                 u'\u5938', u'\u5939', u'\u593a', u'\u5944', u'\u5947', u'\u5948', u'\u5949', u'\u594b',
                 u'\u594f', u'\u5951', u'\u5954', u'\u5955', u'\u5956', u'\u5957', u'\u5960', u'\u5962',
                 u'\u5965', u'\u5973', u'\u5974', u'\u5976', u'\u5978', u'\u5979', u'\u597d', u'\u5982',
                 u'\u5984', u'\u5986', u'\u5987', u'\u5988', u'\u5992', u'\u5993', u'\u5996', u'\u5999',
                 u'\u59a5', u'\u59a8', u'\u59b9', u'\u59bb', u'\u59c6', u'\u59ca', u'\u59cb', u'\u59d0',
                 u'\u59d1', u'\u59d3', u'\u59d4', u'\u59da', u'\u59dc', u'\u59e5', u'\u59e8', u'\u59fb',
                 u'\u59ff', u'\u5a01', u'\u5a03', u'\u5a04', u'\u5a07', u'\u5a18', u'\u5a1c', u'\u5a29',
                 u'\u5a31', u'\u5a36', u'\u5a46', u'\u5a49', u'\u5a5a', u'\u5a74', u'\u5a76', u'\u5a7f',
                 u'\u5a92', u'\u5a9a', u'\u5ab3', u'\u5ac1', u'\u5ac2', u'\u5ac9', u'\u5acc', u'\u5ae1',
                 u'\u5ae9', u'\u5b09', u'\u5b50', u'\u5b54', u'\u5b55', u'\u5b57', u'\u5b58', u'\u5b59',
                 u'\u5b5d', u'\u5b5f', u'\u5b63', u'\u5b64', u'\u5b66', u'\u5b69', u'\u5b75', u'\u5b7d',
                 u'\u5b81', u'\u5b83', u'\u5b85', u'\u5b87', u'\u5b88', u'\u5b89', u'\u5b8b', u'\u5b8c',
                 u'\u5b8f', u'\u5b97', u'\u5b98', u'\u5b99', u'\u5b9a', u'\u5b9b', u'\u5b9c', u'\u5b9d',
                 u'\u5b9e', u'\u5ba0', u'\u5ba1', u'\u5ba2', u'\u5ba3', u'\u5ba4', u'\u5ba6', u'\u5baa',
                 u'\u5bab', u'\u5bb0', u'\u5bb3', u'\u5bb4', u'\u5bb5', u'\u5bb6', u'\u5bb9', u'\u5bbd',
                 u'\u5bbe', u'\u5bbf', u'\u5bc2', u'\u5bc4', u'\u5bc6', u'\u5bc7', u'\u5bcc', u'\u5bd2',
                 u'\u5bd3', u'\u5bdd', u'\u5bde', u'\u5bdf', u'\u5be1', u'\u5be5', u'\u5be8', u'\u5bf8',
                 u'\u5bf9', u'\u5bfa', u'\u5bfb', u'\u5bfc', u'\u5bff', u'\u5c01', u'\u5c04', u'\u5c06',
                 u'\u5c09', u'\u5c0a', u'\u5c0f', u'\u5c11', u'\u5c14', u'\u5c16', u'\u5c18', u'\u5c1a',
                 u'\u5c1d', u'\u5c24', u'\u5c31', u'\u5c38', u'\u5c3a', u'\u5c3c', u'\u5c3d', u'\u5c3e',
                 u'\u5c3f', u'\u5c40', u'\u5c41', u'\u5c42', u'\u5c45', u'\u5c48', u'\u5c49', u'\u5c4a',
                 u'\u5c4b', u'\u5c4e', u'\u5c4f', u'\u5c51', u'\u5c55', u'\u5c5e', u'\u5c60', u'\u5c61',
                 u'\u5c65', u'\u5c6f', u'\u5c71', u'\u5c79', u'\u5c7f', u'\u5c81', u'\u5c82', u'\u5c94',
                 u'\u5c96', u'\u5c97', u'\u5c9b', u'\u5ca9', u'\u5cad', u'\u5cb3', u'\u5cb8', u'\u5ce1',
                 u'\u5ce6', u'\u5ced', u'\u5cf0', u'\u5cfb', u'\u5d07', u'\u5d0e', u'\u5d14', u'\u5d16',
                 u'\u5d29', u'\u5d2d', u'\u5d4c', u'\u5dcd', u'\u5ddd', u'\u5dde', u'\u5de1', u'\u5de2',
                 u'\u5de5', u'\u5de6', u'\u5de7', u'\u5de8', u'\u5de9', u'\u5deb', u'\u5dee', u'\u5df1',
                 u'\u5df2', u'\u5df4', u'\u5df7', u'\u5dfe', u'\u5e01', u'\u5e02', u'\u5e03', u'\u5e05',
                 u'\u5e06', u'\u5e08', u'\u5e0c', u'\u5e10', u'\u5e15', u'\u5e16', u'\u5e18', u'\u5e1a',
                 u'\u5e1c', u'\u5e1d', u'\u5e26', u'\u5e2d', u'\u5e2e', u'\u5e38', u'\u5e3d', u'\u5e45',
                 u'\u5e4c', u'\u5e54', u'\u5e55', u'\u5e62', u'\u5e72', u'\u5e72', u'\u5e73', u'\u5e74',
                 u'\u5e76', u'\u5e78', u'\u5e7b', u'\u5e7c', u'\u5e7d', u'\u5e7f', u'\u5e84', u'\u5e86',
                 u'\u5e87', u'\u5e8a', u'\u5e8f', u'\u5e90', u'\u5e93', u'\u5e94', u'\u5e95', u'\u5e97',
                 u'\u5e99', u'\u5e9c', u'\u5e9e', u'\u5e9f', u'\u5ea6', u'\u5ea7', u'\u5ead', u'\u5eb5',
                 u'\u5eb6', u'\u5eb7', u'\u5eb8', u'\u5ec9', u'\u5eca', u'\u5ed3', u'\u5ef6', u'\u5ef7',
                 u'\u5efa', u'\u5f00', u'\u5f02', u'\u5f03', u'\u5f04', u'\u5f0a', u'\u5f0f', u'\u5f13',
                 u'\u5f15', u'\u5f1b', u'\u5f1f', u'\u5f20', u'\u5f25', u'\u5f26', u'\u5f27', u'\u5f2f',
                 u'\u5f31', u'\u5f39', u'\u5f3a', u'\u5f52', u'\u5f53', u'\u5f55', u'\u5f62', u'\u5f64',
                 u'\u5f69', u'\u5f6a', u'\u5f6c', u'\u5f6d', u'\u5f70', u'\u5f71', u'\u5f79', u'\u5f7b',
                 u'\u5f7c', u'\u5f80', u'\u5f81', u'\u5f84', u'\u5f85', u'\u5f88', u'\u5f8a', u'\u5f8b',
                 u'\u5f90', u'\u5f92', u'\u5f92', u'\u5f97', u'\u5f98', u'\u5fa1', u'\u5faa', u'\u5fae',
                 u'\u5fb7', u'\u5fbd', u'\u5fc3', u'\u5fc5', u'\u5fc6', u'\u5fcc', u'\u5fcd', u'\u5fd7',
                 u'\u5fd8', u'\u5fd9', u'\u5fe0', u'\u5fe7', u'\u5feb', u'\u5ff1', u'\u5ff5', u'\u5ffd',
                 u'\u5fff', u'\u6000', u'\u6001', u'\u600e', u'\u6012', u'\u6014', u'\u6015', u'\u6016',
                 u'\u601c', u'\u601d', u'\u6020', u'\u6025', u'\u6027', u'\u6028', u'\u602a', u'\u602f',
                 u'\u603b', u'\u6043', u'\u604b', u'\u604d', u'\u6050', u'\u6052', u'\u6055', u'\u6062',
                 u'\u6064', u'\u6068', u'\u6069', u'\u606c', u'\u606d', u'\u606f', u'\u6070', u'\u6073',
                 u'\u6076', u'\u607c', u'\u6084', u'\u6089', u'\u608d', u'\u6094', u'\u609f', u'\u60a0',
                 u'\u60a3', u'\u60a6', u'\u60a8', u'\u60ac', u'\u60af', u'\u60b2', u'\u60b4', u'\u60bc',
                 u'\u60c5', u'\u60ca', u'\u60cb', u'\u60d1', u'\u60d5', u'\u60dc', u'\u60e0', u'\u60e6',
                 u'\u60e7', u'\u60e8', u'\u60e9', u'\u60eb', u'\u60ed', u'\u60ef', u'\u60f0', u'\u60f3',
                 u'\u60f6', u'\u60f9', u'\u6101', u'\u6108', u'\u6109', u'\u610f', u'\u6115', u'\u611a',
                 u'\u611f', u'\u6124', u'\u6127', u'\u613f', u'\u6148', u'\u614c', u'\u614e', u'\u6155',
                 u'\u6162', u'\u6167', u'\u6168', u'\u6170', u'\u6177', u'\u618b', u'\u618e', u'\u6194',
                 u'\u61a8', u'\u61be', u'\u61c2', u'\u61c8', u'\u61ca', u'\u61d2', u'\u61e6', u'\u6208',
                 u'\u620f', u'\u6210', u'\u6211', u'\u6212', u'\u6216', u'\u6218', u'\u621a', u'\u622a',
                 u'\u6233', u'\u6234', u'\u6237', u'\u623f', u'\u6240', u'\u6241', u'\u6247', u'\u624b',
                 u'\u624d', u'\u624e', u'\u6251', u'\u6252', u'\u6253', u'\u6254', u'\u6258', u'\u625b',
                 u'\u6263', u'\u6267', u'\u6269', u'\u626b', u'\u626c', u'\u626d', u'\u626e', u'\u626f',
                 u'\u6270', u'\u6273', u'\u6276', u'\u6279', u'\u627c', u'\u627e', u'\u627f', u'\u6280',
                 u'\u6284', u'\u628a', u'\u6291', u'\u6292', u'\u6293', u'\u6295', u'\u6296', u'\u6297',
                 u'\u6298', u'\u629a', u'\u629b', u'\u62a0', u'\u62a1', u'\u62a2', u'\u62a4', u'\u62a5',
                 u'\u62ab', u'\u62ac', u'\u62b1', u'\u62b5', u'\u62b9', u'\u62bc', u'\u62bd', u'\u62c2',
                 u'\u62c4', u'\u62c5', u'\u62c6', u'\u62c7', u'\u62c9', u'\u62cc', u'\u62cd', u'\u62d0',
                 u'\u62d2', u'\u62d3', u'\u62d4', u'\u62d6', u'\u62d7', u'\u62d8', u'\u62d9', u'\u62db',
                 u'\u62dc', u'\u62df', u'\u62e2', u'\u62e3', u'\u62e5', u'\u62e6', u'\u62e7', u'\u62e8',
                 u'\u62e9', u'\u62ec', u'\u62ed', u'\u62ef', u'\u62f1', u'\u62f3', u'\u62f4', u'\u62f7',
                 u'\u62fc', u'\u62fe', u'\u62ff', u'\u6301', u'\u6302', u'\u6307', u'\u6309', u'\u630e',
                 u'\u6311', u'\u6316', u'\u631a', u'\u631f', u'\u6320', u'\u6321', u'\u6323', u'\u6324',
                 u'\u6325', u'\u6328', u'\u632a', u'\u632b', u'\u632f', u'\u633a', u'\u633d', u'\u6342',
                 u'\u6345', u'\u6346', u'\u6349', u'\u634c', u'\u634d', u'\u634e', u'\u634f', u'\u6350',
                 u'\u6355', u'\u635e', u'\u635f', u'\u6361', u'\u6362', u'\u6363', u'\u6367', u'\u636e',
                 u'\u6376', u'\u6377', u'\u637a', u'\u637b', u'\u6380', u'\u6382', u'\u6388', u'\u6389',
                 u'\u638c', u'\u638f', u'\u6390', u'\u6392', u'\u6396', u'\u6398', u'\u63a0', u'\u63a2',
                 u'\u63a5', u'\u63a7', u'\u63a8', u'\u63a9', u'\u63aa', u'\u63b0', u'\u63b7', u'\u63b8',
                 u'\u63ba', u'\u63c9', u'\u63cd', u'\u63cf', u'\u63d0', u'\u63d2', u'\u63d6', u'\u63e1',
                 u'\u63e3', u'\u63e9', u'\u63ea', u'\u63ed', u'\u63f4', u'\u63fd', u'\u6400', u'\u6401',
                 u'\u6402', u'\u6405', u'\u640f', u'\u6413', u'\u6414', u'\u641c', u'\u641e', u'\u642a',
                 u'\u642c', u'\u642d', u'\u643a', u'\u6444', u'\u6446', u'\u6447', u'\u644a', u'\u6454',
                 u'\u6458', u'\u6467', u'\u6469', u'\u6478', u'\u6479', u'\u6487', u'\u6491', u'\u6492',
                 u'\u6495', u'\u649e', u'\u64a4', u'\u64a9', u'\u64ac', u'\u64ad', u'\u64ae', u'\u64b0',
                 u'\u64b5', u'\u64bc', u'\u64c2', u'\u64c5', u'\u64cd', u'\u64ce', u'\u64d2', u'\u64e6',
                 u'\u6500', u'\u6512', u'\u6518', u'\u652f', u'\u6536', u'\u6539', u'\u653b', u'\u653e',
                 u'\u653f', u'\u6545', u'\u6548', u'\u654c', u'\u654f', u'\u6551', u'\u6559', u'\u655b',
                 u'\u655e', u'\u6562', u'\u6563', u'\u6566', u'\u656c', u'\u6570', u'\u6572', u'\u6574',
                 u'\u6577', u'\u6587', u'\u658b', u'\u6591', u'\u6597', u'\u6599', u'\u659c', u'\u659f',
                 u'\u65a4', u'\u65a5', u'\u65a7', u'\u65a9', u'\u65ad', u'\u65af', u'\u65b0', u'\u65b9',
                 u'\u65bd', u'\u65c1', u'\u65c5', u'\u65cb', u'\u65cf', u'\u65d7', u'\u65e0', u'\u65e2',
                 u'\u65e5', u'\u65e6', u'\u65e7', u'\u65e8', u'\u65e9', u'\u65ec', u'\u65ed', u'\u65f1',
                 u'\u65f6', u'\u65f7', u'\u65fa', u'\u6602', u'\u6606', u'\u660c', u'\u660e', u'\u660f',
                 u'\u6613', u'\u6614', u'\u6619', u'\u661f', u'\u6620', u'\u6625', u'\u6627', u'\u6628',
                 u'\u662d', u'\u662f', u'\u6635', u'\u663c', u'\u663e', u'\u6643', u'\u664b', u'\u664c',
                 u'\u6652', u'\u6653', u'\u6655', u'\u665a', u'\u6664', u'\u6666', u'\u6668', u'\u666e',
                 u'\u666f', u'\u6670', u'\u6674', u'\u6676', u'\u667a', u'\u667e', u'\u6682', u'\u6687',
                 u'\u6691', u'\u6696', u'\u6697', u'\u66ae', u'\u66b4', u'\u66d9', u'\u66f2', u'\u66f4',
                 u'\u66f9', u'\u66fc', u'\u66fe', u'\u66ff', u'\u6700', u'\u6708', u'\u6709', u'\u670b',
                 u'\u670d', u'\u6717', u'\u671b', u'\u671d', u'\u671f', u'\u6726', u'\u6728', u'\u672a',
                 u'\u672b', u'\u672c', u'\u672f', u'\u6731', u'\u6734', u'\u6735', u'\u673a', u'\u673d',
                 u'\u6740', u'\u6742', u'\u6743', u'\u6746', u'\u6748', u'\u6749', u'\u674e', u'\u674f',
                 u'\u6750', u'\u6751', u'\u6756', u'\u675c', u'\u675f', u'\u6760', u'\u6761', u'\u6765',
                 u'\u6768', u'\u676d', u'\u676f', u'\u6770', u'\u677e', u'\u677f', u'\u6781', u'\u6784',
                 u'\u6789', u'\u6790', u'\u6795', u'\u6797', u'\u679a', u'\u679c', u'\u679d', u'\u67a2',
                 u'\u67a3', u'\u67aa', u'\u67ab', u'\u67af', u'\u67b6', u'\u67b7', u'\u67c4', u'\u67cf',
                 u'\u67d0', u'\u67d1', u'\u67d2', u'\u67d3', u'\u67d4', u'\u67dc', u'\u67e0', u'\u67e5',
                 u'\u67ec', u'\u67f1', u'\u67f3', u'\u67f4', u'\u67ff', u'\u6805', u'\u6807', u'\u6808',
                 u'\u680b', u'\u680f', u'\u6811', u'\u6813', u'\u6816', u'\u6817', u'\u6821', u'\u682a',
                 u'\u6837', u'\u6838', u'\u6839', u'\u683c', u'\u683d', u'\u6842', u'\u6843', u'\u6845',
                 u'\u6846', u'\u6848', u'\u684c', u'\u6850', u'\u6851', u'\u6863', u'\u6865', u'\u6866',
                 u'\u6868', u'\u6869', u'\u6876', u'\u6881', u'\u6885', u'\u6886', u'\u6897', u'\u68a2',
                 u'\u68a6', u'\u68a7', u'\u68a8', u'\u68ad', u'\u68af', u'\u68b0', u'\u68b3', u'\u68c0',
                 u'\u68c9', u'\u68cb', u'\u68cd', u'\u68d2', u'\u68d5', u'\u68d8', u'\u68da', u'\u68e0',
                 u'\u68ee', u'\u68f1', u'\u68f5', u'\u68fa', u'\u6905', u'\u690d', u'\u690e', u'\u6912',
                 u'\u692d', u'\u6930', u'\u693f', u'\u6954', u'\u695a', u'\u695e', u'\u6963', u'\u6977',
                 u'\u697c', u'\u6982', u'\u6984', u'\u6986', u'\u6994', u'\u6995', u'\u699b', u'\u699c',
                 u'\u69a8', u'\u69b4', u'\u69d0', u'\u69fd', u'\u6a0a', u'\u6a1f', u'\u6a21', u'\u6a2a',
                 u'\u6a31', u'\u6a44', u'\u6a58', u'\u6a59', u'\u6a61', u'\u6a71', u'\u6a80', u'\u6a90',
                 u'\u6aa9', u'\u6aac', u'\u6b20', u'\u6b21', u'\u6b22', u'\u6b23', u'\u6b27', u'\u6b32',
                 u'\u6b3a', u'\u6b3e', u'\u6b47', u'\u6b49', u'\u6b4c', u'\u6b62', u'\u6b63', u'\u6b64',
                 u'\u6b65', u'\u6b66', u'\u6b67', u'\u6b6a', u'\u6b79', u'\u6b7b', u'\u6b7c', u'\u6b83',
                 u'\u6b89', u'\u6b8a', u'\u6b8b', u'\u6b96', u'\u6bb4', u'\u6bb5', u'\u6bb7', u'\u6bbf',
                 u'\u6bc1', u'\u6bc5', u'\u6bcd', u'\u6bcf', u'\u6bd2', u'\u6bd4', u'\u6bd5', u'\u6bd9',
                 u'\u6bdb', u'\u6be1', u'\u6beb', u'\u6bef', u'\u6c0f', u'\u6c11', u'\u6c13', u'\u6c14',
                 u'\u6c1b', u'\u6c22', u'\u6c27', u'\u6c28', u'\u6c2e', u'\u6c2f', u'\u6c34', u'\u6c38',
                 u'\u6c41', u'\u6c42', u'\u6c47', u'\u6c49', u'\u6c57', u'\u6c5b', u'\u6c5e', u'\u6c5f',
                 u'\u6c60', u'\u6c61', u'\u6c64', u'\u6c6a', u'\u6c70', u'\u6c79', u'\u6c7d', u'\u6c83',
                 u'\u6c88', u'\u6c89', u'\u6c90', u'\u6c99', u'\u6c9b', u'\u6c9f', u'\u6ca1', u'\u6ca5',
                 u'\u6ca6', u'\u6ca7', u'\u6caa', u'\u6cab', u'\u6cae', u'\u6cb3', u'\u6cb8', u'\u6cb9',
                 u'\u6cbb', u'\u6cbc', u'\u6cbd', u'\u6cbe', u'\u6cbf', u'\u6cc4', u'\u6cc9', u'\u6cca',
                 u'\u6ccc', u'\u6cd5', u'\u6cdb', u'\u6cde', u'\u6ce1', u'\u6ce2', u'\u6ce3', u'\u6ce5',
                 u'\u6ce8', u'\u6cea', u'\u6cf0', u'\u6cf3', u'\u6cf5', u'\u6cfb', u'\u6cfc', u'\u6cfd',
                 u'\u6d01', u'\u6d0b', u'\u6d12', u'\u6d17', u'\u6d1b', u'\u6d1e', u'\u6d25', u'\u6d2a',
                 u'\u6d32', u'\u6d3b', u'\u6d3c', u'\u6d3d', u'\u6d3e', u'\u6d41', u'\u6d45', u'\u6d46',
                 u'\u6d47', u'\u6d4a', u'\u6d4b', u'\u6d4e', u'\u6d51', u'\u6d53', u'\u6d59', u'\u6d66',
                 u'\u6d69', u'\u6d6a', u'\u6d6e', u'\u6d74', u'\u6d77', u'\u6d78', u'\u6d82', u'\u6d88',
                 u'\u6d89', u'\u6d8c', u'\u6d8e', u'\u6d95', u'\u6d9b', u'\u6d9d', u'\u6da1', u'\u6da3',
                 u'\u6da4', u'\u6da6', u'\u6da7', u'\u6da8', u'\u6da9', u'\u6dae', u'\u6daf', u'\u6db2',
                 u'\u6db5', u'\u6dc0', u'\u6dc6', u'\u6dcb', u'\u6dcc', u'\u6dd1', u'\u6dd8', u'\u6de1',
                 u'\u6de4', u'\u6deb', u'\u6dee', u'\u6df1', u'\u6df3', u'\u6df7', u'\u6df9', u'\u6dfb',
                 u'\u6e05', u'\u6e0a', u'\u6e10', u'\u6e14', u'\u6e17', u'\u6e20', u'\u6e21', u'\u6e23',
                 u'\u6e24', u'\u6e29', u'\u6e2f', u'\u6e34', u'\u6e38', u'\u6e3a', u'\u6e43', u'\u6e56',
                 u'\u6e58', u'\u6e7e', u'\u6e7f', u'\u6e83', u'\u6e85', u'\u6e89', u'\u6e90', u'\u6e9c',
                 u'\u6ea2', u'\u6eaa', u'\u6eaf', u'\u6eb6', u'\u6eba', u'\u6ecb', u'\u6ed1', u'\u6ed3',
                 u'\u6ed4', u'\u6eda', u'\u6ede', u'\u6ee1', u'\u6ee4', u'\u6ee5', u'\u6ee8', u'\u6ee9',
                 u'\u6ef4', u'\u6f02', u'\u6f06', u'\u6f0f', u'\u6f13', u'\u6f14', u'\u6f20', u'\u6f29',
                 u'\u6f2b', u'\u6f31', u'\u6f3e', u'\u6f58', u'\u6f5c', u'\u6f66', u'\u6f6d', u'\u6f6e',
                 u'\u6f84', u'\u6f88', u'\u6f8e', u'\u6f9c', u'\u6fa1', u'\u6fb3', u'\u6fc0', u'\u6fd2',
                 u'\u7011', u'\u704c', u'\u706b', u'\u706d', u'\u706f', u'\u7070', u'\u7075', u'\u7076',
                 u'\u7078', u'\u707c', u'\u707e', u'\u707f', u'\u7089', u'\u708a', u'\u708e', u'\u7092',
                 u'\u7095', u'\u70ab', u'\u70ac', u'\u70ad', u'\u70ae', u'\u70b8', u'\u70b9', u'\u70bc',
                 u'\u70c1', u'\u70c2', u'\u70c8', u'\u70d8', u'\u70d9', u'\u70db', u'\u70df', u'\u70e4',
                 u'\u70e6', u'\u70e7', u'\u70eb', u'\u70ed', u'\u70f9', u'\u710a', u'\u7115', u'\u7119',
                 u'\u711a', u'\u7126', u'\u7130', u'\u7136', u'\u714c', u'\u714e', u'\u715e', u'\u7164',
                 u'\u7167', u'\u716e', u'\u7184', u'\u718a', u'\u718f', u'\u7194', u'\u7199', u'\u719f',
                 u'\u71ac', u'\u71c3', u'\u71ce', u'\u71d5', u'\u71e5', u'\u7206', u'\u722a', u'\u722c',
                 u'\u7231', u'\u7235', u'\u7236', u'\u7237', u'\u7238', u'\u7239', u'\u723d', u'\u7247',
                 u'\u7248', u'\u724c', u'\u724d', u'\u7259', u'\u725b', u'\u7261', u'\u7262', u'\u7267',
                 u'\u7269', u'\u7272', u'\u7275', u'\u7279', u'\u727a', u'\u7280', u'\u7281', u'\u72ac',
                 u'\u72af', u'\u72b6', u'\u72b9', u'\u72c2', u'\u72c8', u'\u72d0', u'\u72d7', u'\u72de',
                 u'\u72e0', u'\u72e1', u'\u72ec', u'\u72ed', u'\u72ee', u'\u72f0', u'\u72f1', u'\u72f8',
                 u'\u72fc', u'\u730e', u'\u7316', u'\u731b', u'\u731c', u'\u7329', u'\u732a', u'\u732b',
                 u'\u732c', u'\u732e', u'\u7334', u'\u733e', u'\u733f', u'\u7384', u'\u7387', u'\u7389',
                 u'\u738b', u'\u7396', u'\u739b', u'\u73a9', u'\u73ab', u'\u73af', u'\u73b0', u'\u73b2',
                 u'\u73b7', u'\u73bb', u'\u73ca', u'\u73cd', u'\u73e0', u'\u73ed', u'\u7403', u'\u7405',
                 u'\u7406', u'\u7409', u'\u7410', u'\u7422', u'\u7433', u'\u7434', u'\u743c', u'\u745e',
                 u'\u745f', u'\u7470', u'\u7483', u'\u74a7', u'\u74dc', u'\u74e2', u'\u74e3', u'\u74e4',
                 u'\u74e6', u'\u74ee', u'\u74f6', u'\u74f7', u'\u7518', u'\u751a', u'\u751c', u'\u751f',
                 u'\u7525', u'\u7528', u'\u7529', u'\u752b', u'\u7530', u'\u7531', u'\u7532', u'\u7533',
                 u'\u7535', u'\u7537', u'\u7538', u'\u753b', u'\u7545', u'\u754c', u'\u754f', u'\u7554',
                 u'\u7559', u'\u755c', u'\u7565', u'\u7566', u'\u756a', u'\u7574', u'\u7578', u'\u7586',
                 u'\u758f', u'\u7591', u'\u7597', u'\u7599', u'\u759a', u'\u759f', u'\u75a4', u'\u75ab',
                 u'\u75ae', u'\u75af', u'\u75b2', u'\u75b9', u'\u75bc', u'\u75be', u'\u75c5', u'\u75c7',
                 u'\u75ca', u'\u75d2', u'\u75d5', u'\u75d8', u'\u75db', u'\u75e2', u'\u75ea', u'\u75f0',
                 u'\u75f4', u'\u75f9', u'\u761f', u'\u7624', u'\u7626', u'\u7629', u'\u762a', u'\u762b',
                 u'\u7638', u'\u763e', u'\u764c', u'\u765e', u'\u7663', u'\u767b', u'\u767d', u'\u767e',
                 u'\u7682', u'\u7684', u'\u7686', u'\u7687', u'\u76ae', u'\u76b1', u'\u76bf', u'\u76c5',
                 u'\u76c6', u'\u76c8', u'\u76ca', u'\u76cf', u'\u76d0', u'\u76d1', u'\u76d2', u'\u76d4',
                 u'\u76d6', u'\u76d7', u'\u76d8', u'\u76db', u'\u76df', u'\u76ee', u'\u76ef', u'\u76f2',
                 u'\u76f4', u'\u76f8', u'\u76f9', u'\u76fc', u'\u76fe', u'\u7701', u'\u7709', u'\u770b',
                 u'\u771f', u'\u7720', u'\u7728', u'\u772f', u'\u7736', u'\u7737', u'\u773c', u'\u7740',
                 u'\u7741', u'\u775b', u'\u7761', u'\u7763', u'\u7766', u'\u776c', u'\u7779', u'\u7784',
                 u'\u778e', u'\u7792', u'\u77a7', u'\u77aa', u'\u77ac', u'\u77ad', u'\u77b3', u'\u77bb',
                 u'\u77d7', u'\u77db', u'\u77e2', u'\u77e5', u'\u77e9', u'\u77eb', u'\u77ed', u'\u77ee',
                 u'\u77f3', u'\u77fe', u'\u77ff', u'\u7801', u'\u7802', u'\u780c', u'\u780d', u'\u7814',
                 u'\u7816', u'\u781a', u'\u7830', u'\u7834', u'\u7838', u'\u783e', u'\u7840', u'\u7845',
                 u'\u7855', u'\u785d', u'\u786b', u'\u786c', u'\u786e', u'\u787c', u'\u7889', u'\u788c',
                 u'\u788d', u'\u788e', u'\u7891', u'\u7897', u'\u7898', u'\u789f', u'\u78a7', u'\u78b0',
                 u'\u78b1', u'\u78b3', u'\u78b4', u'\u78be', u'\u78c1', u'\u78c5', u'\u78d5', u'\u78e8',
                 u'\u78f7', u'\u78fa', u'\u7901', u'\u793a', u'\u793c', u'\u793e', u'\u7948', u'\u7956',
                 u'\u795d', u'\u795e', u'\u795f', u'\u7960', u'\u7965', u'\u7968', u'\u796d', u'\u7977',
                 u'\u7978', u'\u7980', u'\u7981', u'\u798f', u'\u79bb', u'\u79bd', u'\u79be', u'\u79c0',
                 u'\u79c1', u'\u79c3', u'\u79c6', u'\u79c9', u'\u79cb', u'\u79cd', u'\u79d1', u'\u79d2',
                 u'\u79d5', u'\u79d8', u'\u79df', u'\u79e4', u'\u79e6', u'\u79e7', u'\u79e9', u'\u79eb',
                 u'\u79ef', u'\u79f0', u'\u79f8', u'\u79fb', u'\u79fd', u'\u7a00', u'\u7a0b', u'\u7a0d',
                 u'\u7a0e', u'\u7a1a', u'\u7a20', u'\u7a33', u'\u7a3b', u'\u7a3c', u'\u7a3d', u'\u7a3f',
                 u'\u7a46', u'\u7a57', u'\u7a74', u'\u7a76', u'\u7a77', u'\u7a7a', u'\u7a7f', u'\u7a81',
                 u'\u7a83', u'\u7a84', u'\u7a8d', u'\u7a91', u'\u7a92', u'\u7a96', u'\u7a97', u'\u7a98',
                 u'\u7a9c', u'\u7a9d', u'\u7a9f', u'\u7aa5', u'\u7abf', u'\u7acb', u'\u7ad6', u'\u7ad9',
                 u'\u7ade', u'\u7adf', u'\u7ae0', u'\u7ae3', u'\u7ae5', u'\u7aed', u'\u7aef', u'\u7af9',
                 u'\u7aff', u'\u7b06', u'\u7b0b', u'\u7b11', u'\u7b14', u'\u7b19', u'\u7b1b', u'\u7b24',
                 u'\u7b26', u'\u7b28', u'\u7b2c', u'\u7b3c', u'\u7b49', u'\u7b4b', u'\u7b4f', u'\u7b50',
                 u'\u7b51', u'\u7b52', u'\u7b54', u'\u7b56', u'\u7b5b', u'\u7b5d', u'\u7b77', u'\u7b79',
                 u'\u7b7e', u'\u7b80', u'\u7b8d', u'\u7b95', u'\u7b97', u'\u7ba1', u'\u7ba9', u'\u7bab',
                 u'\u7bad', u'\u7bb1', u'\u7bc7', u'\u7bd3', u'\u7bd9', u'\u7be1', u'\u7bee', u'\u7bf1',
                 u'\u7bf7', u'\u7c07', u'\u7c38', u'\u7c3f', u'\u7c4d', u'\u7c73', u'\u7c7b', u'\u7c7d',
                 u'\u7c89', u'\u7c92', u'\u7c97', u'\u7c98', u'\u7c9f', u'\u7ca4', u'\u7ca5', u'\u7caa',
                 u'\u7cae', u'\u7cb1', u'\u7cb9', u'\u7cbe', u'\u7cca', u'\u7cd5', u'\u7cd6', u'\u7cd9',
                 u'\u7cdc', u'\u7cdf', u'\u7ce0', u'\u7cef', u'\u7cfb', u'\u7d0a', u'\u7d20', u'\u7d22',
                 u'\u7d27', u'\u7d2b', u'\u7d2f', u'\u7d6e', u'\u7e41', u'\u7ea0', u'\u7ea2', u'\u7ea4',
                 u'\u7ea6', u'\u7ea7', u'\u7eaa', u'\u7eab', u'\u7eac', u'\u7eaf', u'\u7eb1', u'\u7eb2',
                 u'\u7eb3', u'\u7eb5', u'\u7eb7', u'\u7eb8', u'\u7eb9', u'\u7eba', u'\u7ebd', u'\u7ebf',
                 u'\u7ec3', u'\u7ec4', u'\u7ec5', u'\u7ec6', u'\u7ec7', u'\u7ec8', u'\u7eca', u'\u7ecd',
                 u'\u7ece', u'\u7ecf', u'\u7ed1', u'\u7ed2', u'\u7ed3', u'\u7ed5', u'\u7ed8', u'\u7ed9',
                 u'\u7edc', u'\u7edd', u'\u7ede', u'\u7edf', u'\u7ee2', u'\u7ee3', u'\u7ee7', u'\u7ee9',
                 u'\u7eea', u'\u7eed', u'\u7ef0', u'\u7ef3', u'\u7ef4', u'\u7ef5', u'\u7ef7', u'\u7ef8',
                 u'\u7efc', u'\u7efd', u'\u7eff', u'\u7f00', u'\u7f05', u'\u7f06', u'\u7f0e', u'\u7f13',
                 u'\u7f14', u'\u7f15', u'\u7f16', u'\u7f18', u'\u7f1a', u'\u7f1d', u'\u7f20', u'\u7f24',
                 u'\u7f28', u'\u7f29', u'\u7f2d', u'\u7f30', u'\u7f34', u'\u7f38', u'\u7f3a', u'\u7f50',
                 u'\u7f51', u'\u7f55', u'\u7f57', u'\u7f5a', u'\u7f62', u'\u7f69', u'\u7f6a', u'\u7f6e',
                 u'\u7f72', u'\u7f8a', u'\u7f8e', u'\u7f94', u'\u7f9e', u'\u7fa1', u'\u7fa4', u'\u7fb9',
                 u'\u7fbd', u'\u7fc1', u'\u7fc5', u'\u7fce', u'\u7fd4', u'\u7fd8', u'\u7fe0', u'\u7fe9',
                 u'\u7ff0', u'\u7ffb', u'\u7ffc', u'\u8000', u'\u8001', u'\u8003', u'\u8005', u'\u800c',
                 u'\u800d', u'\u8010', u'\u8015', u'\u8015', u'\u8017', u'\u8019', u'\u8033', u'\u8038',
                 u'\u803b', u'\u803d', u'\u803f', u'\u8042', u'\u804a', u'\u804b', u'\u804c', u'\u8054',
                 u'\u8058', u'\u805a', u'\u806a', u'\u8083', u'\u8084', u'\u8086', u'\u8089', u'\u808b',
                 u'\u808c', u'\u8096', u'\u8098', u'\u809a', u'\u809b', u'\u809d', u'\u80a0', u'\u80a1',
                 u'\u80a2', u'\u80a4', u'\u80a5', u'\u80a9', u'\u80aa', u'\u80ae', u'\u80af', u'\u80b2',
                 u'\u80b4', u'\u80ba', u'\u80be', u'\u80bf', u'\u80c0', u'\u80c1', u'\u80c3', u'\u80c6',
                 u'\u80cc', u'\u80ce', u'\u80d6', u'\u80da', u'\u80dc', u'\u80de', u'\u80e1', u'\u80e7',
                 u'\u80ef', u'\u80f0', u'\u80f3', u'\u80f6', u'\u80f8', u'\u80fd', u'\u8102', u'\u8106',
                 u'\u8109', u'\u810a', u'\u810f', u'\u8110', u'\u8111', u'\u8113', u'\u8116', u'\u811a',
                 u'\u812f', u'\u8131', u'\u8138', u'\u813e', u'\u814a', u'\u814b', u'\u814c', u'\u8150',
                 u'\u8154', u'\u8155', u'\u8165', u'\u816e', u'\u8170', u'\u8179', u'\u817a', u'\u817b',
                 u'\u817e', u'\u817f', u'\u8180', u'\u818a', u'\u818f', u'\u8198', u'\u819b', u'\u819c',
                 u'\u819d', u'\u81a8', u'\u81b3', u'\u81c0', u'\u81c2', u'\u81ca', u'\u81e3', u'\u81ea',
                 u'\u81ed', u'\u81f3', u'\u81f4', u'\u81fc', u'\u8200', u'\u8205', u'\u8206', u'\u820c',
                 u'\u820d', u'\u8212', u'\u8214', u'\u821e', u'\u821f', u'\u822a', u'\u822c', u'\u8230',
                 u'\u8231', u'\u8235', u'\u8236', u'\u8237', u'\u8239', u'\u8247', u'\u8258', u'\u826f',
                 u'\u8270', u'\u8272', u'\u8273', u'\u827a', u'\u827e', u'\u8282', u'\u828b', u'\u828d',
                 u'\u8292', u'\u8299', u'\u829c', u'\u829d', u'\u82a5', u'\u82a6', u'\u82ac', u'\u82ad',
                 u'\u82af', u'\u82b1', u'\u82b3', u'\u82b9', u'\u82bd', u'\u82c7', u'\u82cd', u'\u82cf',
                 u'\u82d4', u'\u82d7', u'\u82db', u'\u82de', u'\u82df', u'\u82e5', u'\u82e6', u'\u82eb',
                 u'\u82f1', u'\u82f9', u'\u8301', u'\u8302', u'\u8303', u'\u8304', u'\u8305', u'\u8309',
                 u'\u830e', u'\u8327', u'\u832b', u'\u832c', u'\u8334', u'\u8335', u'\u8336', u'\u8338',
                 u'\u8346', u'\u8349', u'\u8350', u'\u8352', u'\u8354', u'\u835a', u'\u835e', u'\u8360',
                 u'\u8361', u'\u8363', u'\u8364', u'\u8367', u'\u836f', u'\u8377', u'\u8378', u'\u8389',
                 u'\u83ab', u'\u83b1', u'\u83b2', u'\u83b7', u'\u83b9', u'\u83ba', u'\u83bd', u'\u83c7',
                 u'\u83ca', u'\u83cc', u'\u83dc', u'\u83e0', u'\u83e9', u'\u83f1', u'\u83f2', u'\u8404',
                 u'\u840c', u'\u840d', u'\u840e', u'\u841d', u'\u8424', u'\u8425', u'\u8427', u'\u8428',
                 u'\u843d', u'\u8457', u'\u845b', u'\u8461', u'\u8463', u'\u846b', u'\u846c', u'\u8471',
                 u'\u8475', u'\u8482', u'\u848b', u'\u8499', u'\u849c', u'\u84b2', u'\u84b8', u'\u84bf',
                 u'\u84c4', u'\u84c9', u'\u84d6', u'\u84dd', u'\u84ec', u'\u8511', u'\u8513', u'\u8517',
                 u'\u851a', u'\u852b', u'\u852c', u'\u853c', u'\u853d', u'\u8549', u'\u854a', u'\u8574',
                 u'\u857e', u'\u8584', u'\u8587', u'\u859b', u'\u85aa', u'\u85af', u'\u85cf', u'\u85d0',
                 u'\u85d5', u'\u85e4', u'\u85fb', u'\u8611', u'\u8638', u'\u864e', u'\u864f', u'\u8650',
                 u'\u8651', u'\u865a', u'\u866b', u'\u8671', u'\u8679', u'\u867d', u'\u867e', u'\u8680',
                 u'\u8681', u'\u8682', u'\u868a', u'\u868c', u'\u8693', u'\u8695', u'\u869c', u'\u86a3',
                 u'\u86a4', u'\u86aa', u'\u86af', u'\u86c0', u'\u86c6', u'\u86c7', u'\u86c9', u'\u86cb',
                 u'\u86d4', u'\u86d9', u'\u86db', u'\u86e4', u'\u86ee', u'\u86f9', u'\u86fe', u'\u8700',
                 u'\u8702', u'\u8708', u'\u8712', u'\u8713', u'\u8715', u'\u8717', u'\u8718', u'\u871c',
                 u'\u8721', u'\u873b', u'\u8747', u'\u8749', u'\u874c', u'\u874e', u'\u8757', u'\u8759',
                 u'\u8760', u'\u8774', u'\u8776', u'\u8783', u'\u878d', u'\u879f', u'\u87ba', u'\u87c0',
                 u'\u87c6', u'\u87cb', u'\u87f9', u'\u8815', u'\u8822', u'\u8840', u'\u8845', u'\u884c',
                 u'\u884d', u'\u8854', u'\u8857', u'\u8859', u'\u8861', u'\u8863', u'\u8865', u'\u8868',
                 u'\u8869', u'\u886b', u'\u886c', u'\u8870', u'\u8877', u'\u8881', u'\u8884', u'\u888b',
                 u'\u888d', u'\u8892', u'\u8896', u'\u889c', u'\u88ab', u'\u88ad', u'\u88b1', u'\u88c1',
                 u'\u88c2', u'\u88c5', u'\u88c6', u'\u88c9', u'\u88d5', u'\u88d9', u'\u88e4', u'\u88f3',
                 u'\u88f8', u'\u88f9', u'\u8902', u'\u8910', u'\u8912', u'\u8925', u'\u895f', u'\u897f',
                 u'\u8981', u'\u8986', u'\u89c1', u'\u89c2', u'\u89c4', u'\u89c5', u'\u89c6', u'\u89c8',
                 u'\u89c9', u'\u89d2', u'\u89e3', u'\u89e6', u'\u8a00', u'\u8a89', u'\u8a8a', u'\u8a93',
                 u'\u8b66', u'\u8b6c', u'\u8ba1', u'\u8ba2', u'\u8ba4', u'\u8ba5', u'\u8ba8', u'\u8ba9',
                 u'\u8bad', u'\u8bae', u'\u8baf', u'\u8bb0', u'\u8bb2', u'\u8bb3', u'\u8bb6', u'\u8bb8',
                 u'\u8bb9', u'\u8bba', u'\u8bbc', u'\u8bbd', u'\u8bbe', u'\u8bbf', u'\u8bc0', u'\u8bc1',
                 u'\u8bc4', u'\u8bc5', u'\u8bc6', u'\u8bc8', u'\u8bc9', u'\u8bca', u'\u8bcd', u'\u8bd1',
                 u'\u8bd5', u'\u8bd7', u'\u8bda', u'\u8bdd', u'\u8bde', u'\u8be1', u'\u8be2', u'\u8be5',
                 u'\u8be6', u'\u8beb', u'\u8bec', u'\u8bed', u'\u8bef', u'\u8bf1', u'\u8bf2', u'\u8bf4',
                 u'\u8bf5', u'\u8bf7', u'\u8bf8', u'\u8bfa', u'\u8bfb', u'\u8bfd', u'\u8bfe', u'\u8c01',
                 u'\u8c03', u'\u8c05', u'\u8c06', u'\u8c08', u'\u8c0a', u'\u8c0b', u'\u8c0d', u'\u8c0e',
                 u'\u8c10', u'\u8c12', u'\u8c13', u'\u8c1a', u'\u8c1c', u'\u8c22', u'\u8c23', u'\u8c24',
                 u'\u8c26', u'\u8c28', u'\u8c2c', u'\u8c2d', u'\u8c31', u'\u8c34', u'\u8c37', u'\u8c41',
                 u'\u8c46', u'\u8c4c', u'\u8c61', u'\u8c6a', u'\u8c6b', u'\u8c79', u'\u8c7a', u'\u8c8c',
                 u'\u8d1d', u'\u8d1e', u'\u8d1f', u'\u8d21', u'\u8d22', u'\u8d23', u'\u8d24', u'\u8d25',
                 u'\u8d26', u'\u8d27', u'\u8d27', u'\u8d28', u'\u8d29', u'\u8d2a', u'\u8d2b', u'\u8d2c',
                 u'\u8d2d', u'\u8d2e', u'\u8d2f', u'\u8d30', u'\u8d31', u'\u8d34', u'\u8d35', u'\u8d38',
                 u'\u8d39', u'\u8d3a', u'\u8d3c', u'\u8d3e', u'\u8d3f', u'\u8d41', u'\u8d42', u'\u8d43',
                 u'\u8d44', u'\u8d4a', u'\u8d4b', u'\u8d4c', u'\u8d4e', u'\u8d4f', u'\u8d50', u'\u8d54',
                 u'\u8d56', u'\u8d58', u'\u8d5a', u'\u8d5b', u'\u8d5e', u'\u8d60', u'\u8d61', u'\u8d62',
                 u'\u8d64', u'\u8d66', u'\u8d6b', u'\u8d70', u'\u8d74', u'\u8d75', u'\u8d76', u'\u8d77',
                 u'\u8d81', u'\u8d85', u'\u8d8a', u'\u8d8b', u'\u8d9f', u'\u8da3', u'\u8db3', u'\u8db4',
                 u'\u8dbe', u'\u8dc3', u'\u8dcb', u'\u8dcc', u'\u8dd1', u'\u8ddb', u'\u8ddd', u'\u8ddf',
                 u'\u8de8', u'\u8dea', u'\u8def', u'\u8df3', u'\u8df5', u'\u8df7', u'\u8dfa', u'\u8e0a',
                 u'\u8e0f', u'\u8e22', u'\u8e29', u'\u8e2a', u'\u8e31', u'\u8e42', u'\u8e44', u'\u8e48',
                 u'\u8e4b', u'\u8e66', u'\u8e6c', u'\u8e6d', u'\u8e72', u'\u8e81', u'\u8e8f', u'\u8eab',
                 u'\u8eac', u'\u8eaf', u'\u8eb2', u'\u8eba', u'\u8f66', u'\u8f67', u'\u8f68', u'\u8f69',
                 u'\u8f6c', u'\u8f6e', u'\u8f6f', u'\u8f70', u'\u8f74', u'\u8f7b', u'\u8f7d', u'\u8f7f',
                 u'\u8f83', u'\u8f85', u'\u8f86', u'\u8f88', u'\u8f89', u'\u8f90', u'\u8f91', u'\u8f93',
                 u'\u8f95', u'\u8f96', u'\u8f99', u'\u8f9b', u'\u8f9c', u'\u8f9e', u'\u8f9f', u'\u8fa3',
                 u'\u8fa8', u'\u8fa9', u'\u8fab', u'\u8fb0', u'\u8fb1', u'\u8fb9', u'\u8fbd', u'\u8fbe',
                 u'\u8fc1', u'\u8fc2', u'\u8fc4', u'\u8fc5', u'\u8fc7', u'\u8fc8', u'\u8fce', u'\u8fd0',
                 u'\u8fd1', u'\u8fd4', u'\u8fd8', u'\u8fd9', u'\u8fdb', u'\u8fdc', u'\u8fdd', u'\u8fde',
                 u'\u8fdf', u'\u8feb', u'\u8ff0', u'\u8ff7', u'\u8ff9', u'\u8ffd', u'\u9000', u'\u9001',
                 u'\u9002', u'\u9003', u'\u9006', u'\u9009', u'\u900a', u'\u900f', u'\u9010', u'\u9012',
                 u'\u9014', u'\u9017', u'\u901a', u'\u901b', u'\u901d', u'\u901e', u'\u901f', u'\u9020',
                 u'\u9022', u'\u902e', u'\u9038', u'\u903b', u'\u903c', u'\u903e', u'\u9042', u'\u9047',
                 u'\u904d', u'\u904f', u'\u9053', u'\u9057', u'\u9063', u'\u9065', u'\u906d', u'\u906e',
                 u'\u9075', u'\u907f', u'\u9080', u'\u9091', u'\u9093', u'\u90a2', u'\u90a3', u'\u90a6',
                 u'\u90aa', u'\u90ae', u'\u90bb', u'\u90c1', u'\u90ca', u'\u90ce', u'\u90d1', u'\u90e8',
                 u'\u90ed', u'\u90fd', u'\u9119', u'\u914c', u'\u914d', u'\u9152', u'\u9157', u'\u915d',
                 u'\u9163', u'\u9165', u'\u916a', u'\u916c', u'\u9171', u'\u9175', u'\u9177', u'\u9178',
                 u'\u917f', u'\u9187', u'\u9189', u'\u918b', u'\u9192', u'\u91c7', u'\u91ca', u'\u91cc',
                 u'\u91cd', u'\u91ce', u'\u91cf', u'\u91d1', u'\u9274', u'\u9488', u'\u9489', u'\u9493',
                 u'\u9499', u'\u949d', u'\u949e', u'\u949f', u'\u94a0', u'\u94a2', u'\u94a5', u'\u94a6',
                 u'\u94a7', u'\u94a9', u'\u94ae', u'\u94b1', u'\u94b3', u'\u94bb', u'\u94be', u'\u94c1',
                 u'\u94c3', u'\u94c5', u'\u94c6', u'\u94d0', u'\u94db', u'\u94dc', u'\u94dd', u'\u94e1',
                 u'\u94e3', u'\u94ed', u'\u94f2', u'\u94f6', u'\u94f8', u'\u94fa', u'\u94fe', u'\u9500',
                 u'\u9501', u'\u9504', u'\u9505', u'\u9508', u'\u9509', u'\u950b', u'\u950c', u'\u9510',
                 u'\u9519', u'\u951a', u'\u9521', u'\u9523', u'\u9524', u'\u9525', u'\u9526', u'\u9528',
                 u'\u952d', u'\u952e', u'\u952f', u'\u9530', u'\u9539', u'\u953b', u'\u9540', u'\u9547',
                 u'\u954a', u'\u9550', u'\u955c', u'\u9563', u'\u9570', u'\u9576', u'\u957f', u'\u95e8',
                 u'\u95ea', u'\u95ed', u'\u95ee', u'\u95ef', u'\u95f0', u'\u95f2', u'\u95f4', u'\u95f7',
                 u'\u95f8', u'\u95f9', u'\u95fa', u'\u95fb', u'\u95fd', u'\u9600', u'\u9601', u'\u9605',
                 u'\u960e', u'\u9610', u'\u9614', u'\u961f', u'\u9631', u'\u9632', u'\u9633', u'\u9634',
                 u'\u9635', u'\u9636', u'\u963b', u'\u963f', u'\u9644', u'\u9645', u'\u9646', u'\u9648',
                 u'\u964b', u'\u964c', u'\u964d', u'\u9650', u'\u9655', u'\u9661', u'\u9662', u'\u9664',
                 u'\u9668', u'\u9669', u'\u966a', u'\u9675', u'\u9676', u'\u9677', u'\u9685', u'\u9686',
                 u'\u968f', u'\u9690', u'\u9694', u'\u9698', u'\u9699', u'\u969c', u'\u96a7', u'\u96b6',
                 u'\u96be', u'\u96c0', u'\u96c1', u'\u96c4', u'\u96c5', u'\u96c6', u'\u96c7', u'\u96cc',
                 u'\u96cf', u'\u96d5', u'\u96e8', u'\u96ea', u'\u96f3', u'\u96f6', u'\u96f7', u'\u96f9',
                 u'\u96fe', u'\u9700', u'\u9707', u'\u9709', u'\u970d', u'\u970e', u'\u971c', u'\u971e',
                 u'\u9732', u'\u9738', u'\u9739', u'\u9752', u'\u9756', u'\u9759', u'\u975e', u'\u9760',
                 u'\u9761', u'\u9762', u'\u9769', u'\u9774', u'\u9776', u'\u978b', u'\u978d', u'\u97a0',
                 u'\u97ad', u'\u97e7', u'\u97e9', u'\u97ed', u'\u97f3', u'\u97f5', u'\u9875', u'\u9876',
                 u'\u9877', u'\u9879', u'\u987a', u'\u987b', u'\u987d', u'\u987e', u'\u987f', u'\u9881',
                 u'\u9882', u'\u9884', u'\u9885', u'\u9886', u'\u9887', u'\u9888', u'\u988a', u'\u9891',
                 u'\u9893', u'\u9896', u'\u9897', u'\u9898', u'\u989c', u'\u989d', u'\u98a0', u'\u98a4',
                 u'\u98ce', u'\u98d2', u'\u98d8', u'\u98de', u'\u98df', u'\u9910', u'\u9965', u'\u996d',
                 u'\u996e', u'\u9970', u'\u9971', u'\u9972', u'\u9975', u'\u9976', u'\u997a', u'\u997c',
                 u'\u997f', u'\u9981', u'\u9985', u'\u9986', u'\u998b', u'\u998d', u'\u998f', u'\u9992',
                 u'\u9996', u'\u9999', u'\u9a6c', u'\u9a6e', u'\u9a6f', u'\u9a70', u'\u9a71', u'\u9a73',
                 u'\u9a74', u'\u9a76', u'\u9a79', u'\u9a7b', u'\u9a7c', u'\u9a7e', u'\u9a82', u'\u9a84',
                 u'\u9a86', u'\u9a87', u'\u9a8c', u'\u9a8f', u'\u9a91', u'\u9a97', u'\u9a9a', u'\u9aa1',
                 u'\u9aa4', u'\u9aa8', u'\u9ad3', u'\u9ad8', u'\u9b13', u'\u9b3c', u'\u9b41', u'\u9b42',
                 u'\u9b44', u'\u9b4f', u'\u9b54', u'\u9c7c', u'\u9c81', u'\u9c9c', u'\u9ca4', u'\u9cab',
                 u'\u9cb8', u'\u9cc4', u'\u9ccd', u'\u9cd6', u'\u9cde', u'\u9e1f', u'\u9e20', u'\u9e21',
                 u'\u9e23', u'\u9e25', u'\u9e26', u'\u9e2d', u'\u9e2f', u'\u9e33', u'\u9e35', u'\u9e3d',
                 u'\u9e3f', u'\u9e43', u'\u9e45', u'\u9e49', u'\u9e4a', u'\u9e4f', u'\u9e64', u'\u9e66',
                 u'\u9e70', u'\u9e7f', u'\u9ea6', u'\u9eb8', u'\u9ebb', u'\u9ec4', u'\u9ecd', u'\u9ece',
                 u'\u9ed1', u'\u9ed4', u'\u9ed8', u'\u9f0e', u'\u9f13', u'\u9f20', u'\u9f3b', u'\u9f50',
                 u'\u9f7f', u'\u9f84', u'\u9f99', u'\u9f9f']


def list_file():
    global all_file
    file_dir = "." + os.sep
    for files in os.listdir(file_dir):
        all_file.append(files)


if __name__ == '__main__':
    list_file()
    # This is a test demo
    # result_test = []
    # result = []
    # for file_name in ss:
    #     print chardet.detect(file_name)
    # print test[1]
    rename_file = {}
    ss = ['\xc4\xe3\xca\xc7.txt',  '\xe6\x88\x91\xe6\x98\xaf.txt', 
          '\xd5\xe2\xca\xc7\xd2\xbb\xca\xd7\xbc\xf2\xb5\xa5\xb5\xc4\xd0\xa1\xc7\xe9\xb8\xe8.txt']
    print ss[0].decode('gb2312')
    tt = [ss[0].decode('utf-8', 'replace')]
    for key in tt[0]:
        print key
    all_file.extend(ss)
    for file_name in all_file:
        result = chardet.detect(file_name)
        # print chardet.detect(file_name)
        if result['confidence'] > 0.8:
            # print result['encoding']
            if result['encoding'] != 'ascii' and result['encoding'] != 'utf-8':
                print "------------------------------------------------------"
                print "chardet predict " + file_name + " encoding is" + result['encoding']
                print file_name + " will rename to " + file_name.decode(result['encoding'],  'replace').encode('utf-8',
                                                                                                              'replace')
                rename_file[file_name] = file_name.decode(result['encoding'],  'replace').encode('utf-8',  'replace')
        elif result['confidence'] > 0.2:
            # use predict way
            flag = 0
            decoded_num = file_name.decode(result['encoding'],  'replace')
            for index in decoded_num:
                if index in unicode_value:
                    flag = 1
                else:
                    temp = chardet.detect(index.encode(result['encoding'],  'replace'))
                    if temp['encoding'] == 'ascii' and temp['confidence'] > 0.9:
                        flag = 1
                    else:
                        flag = 0
                        break
            if 1 == flag:
                print "------------------------------------------------------"
                print file_name + " will rename to " + file_name.decode(result['encoding'],  'replace').encode('utf-8',
                                                                                                              'replace')
                rename_file[file_name] = file_name.decode(result['encoding'],  'replace').encode('utf-8',  'replace')
            else:
                # use utf-8 detect
                flag = 0
                decoded_num = file_name.decode('utf-8',  'replace')
                for index in decoded_num:
                    if index in unicode_value:
                        flag = 1
                    else:
                        temp = chardet.detect(index.encode('utf-8',  'replace'))
                        if temp['encoding'] == 'ascii' and temp['confidence'] > 0.9:
                            flag = 1
                        else:
                            flag = 0
                            break
                if 1 == flag:
                    print "------------------------------------------------------"
                    print file_name + " will rename to " + file_name.decode('utf-8',  'replace').encode('utf-8','replace')
                    rename_file[file_name] = file_name.decode('utf-8',  'replace').encode('utf-8',  'replace')
                else:
                    # use gb2312 detect
                    flag = 0
                    decoded_num = file_name.decode('gb2312', 'replace')
                    for index in decoded_num:
                        if index in unicode_value:
                            flag = 1
                        else:
                            temp = chardet.detect(index.encode('gb2312',  'replace'))
                            if temp['encoding'] == 'ascii' and temp['confidence'] > 0.9:
                                flag = 1
                            else:
                                flag = 0
                                break
                    if 1 == flag:
                        print "------------------------------------------------------"
                        print file_name + " will rename to " + file_name.decode('gb2312',  'replace').encode('utf-8',
                                                                                                            'replace')
                        rename_file[file_name] = file_name.decode('gb2312',  'replace').encode('utf-8',  'replace')
                    else:
                        # use big5 detect
                        flag = 0
                        decoded_num = file_name.decode('big5', 'replace')
                        for index in decoded_num:
                            if index in unicode_value:
                                flag = 1
                            else:
                                temp = chardet.detect(index.encode('big5',  'replace'))
                                if temp['encoding'] == 'ascii' and temp['confidence'] > 0.9:
                                    flag = 1
                                else:
                                    flag = 0
                                    break
                        if 1 == flag:
                            print "------------------------------------------------------"
                            print file_name + " will rename to " + file_name.decode('big5',  'replace').encode('utf-8',
                                                                                                              'replace')
                            rename_file[file_name] = file_name.decode('big5',  'replace').encode('utf-8',  'replace')
        else:
            print "------------------------------------------------------"
            print "chardet predict " + file_name + " encoding is" + result[
                'encoding'] + " but the confidence is too low"
    judge = raw_input("Do you wanna use the plan? (Y/N)")
    if 'Y' == judge or 'y' == judge:
        # record the change to backup the file_name
        for key in rename_file:
            fd = open('change_name_plan.txt',  'a+')
            fd.write(key + ':' + rename_file[key] + '\n')
            # rename will happen in here
            # os.rename(key,  rename_file[key])
    elif 'N' == judge or 'n' == judge:
        print 'Thank for use'
        try:
            sys.exit(0)
        finally:
            print('clean-up')
    else:
        print 'bad input' + '\n'
# end
