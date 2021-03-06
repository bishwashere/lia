PYTHON = ('python', '(\spython( |$|.|,$\n))')
JAVA = ('jsp', '(\s((jsp)|(Java\sServer\sPages)|(Servlets))( |$|.|,))')
KEYWORD_LIST = [
	('php', '\sphp( |$|.|,)'),
	('vsts', '\svsts( |$|.|,)'),
	('jenkins', '\sjenkins( |$|.|,)'),
	('travis', '\stravis( |$|.|,)'),
	('topcoder', '(\s(topcoder)( |$|.|,))'),
	('Typescript', '(\s(ts|typescript)( |$|.|,))'),
	('sap', '(\ssap( |$|.|,))'),
	('conflict resolution', '(\sconflict\s?resolution( |$|.|,))'),
	('Microservices', '(\sMicroservices( |$|.|,))'),
	('monitoring', '(\smonitoring( |$|.|,))'),
	('AWS Lambda', '(\sAWS\s?Lambda( |$|.|,))'),
	('AWS ECS', '(\sAWS\s?ECS( |$|.|,))'),
	('Stored Procedures', '(\sStored\sProcedures( |$|.|,))'),
	('visual studio', '(\svisual\s?studio( |$|.|,))'),
	('vb', '(\svb( |$|.|,))'),
	('communication', '(\s(strong|good|excellent)\s?communication( |$|.|,))'),
	('rest', '(\srest( |$|.|,))'),
	('post', '(\spost( |$|.|,))'),
	('spring', '(\sspring( |$|.|,))'),
	('kubernetes', '(\skubernetes\s?rank( |$|.|,))'),
	('hackerRank', '(\shacker\s?rank( |$|.|,))'),
	('java', '(\sjava( |$|.|,))'),
	('javascript', '(\s(javascript|JS)( |$|.|,))'),
	('json', '(\sjson( |$|.|,))'),
	('soap', '(\ssoap( |$|.|,))'),
	('css', '(\scss( |$|.|,))'),
	('sql', '(\ssql( |$|.|,))'),
	('git', '(\sgit( |$|.|,))'),
	('nosql', '(\snosql( |$|.|,))'),
	('spring', '(\sspring( |$|.|,))'),
	('unit test', '(\sunit\s?test( |$|.|,))'),
	('agile', '(\sagile( |$|.|,))'),
	('CI/CD', '(\s((ci\/cd)|(continuous\sintegration))( |$|.|,))'),
	PYTHON,
	('react', '(\sreact( |$|.|,))'),
	('docker', '(\sdocker( |$|.|,))'),
	('postgres', '(\spostgres( |$|.|,))'),
	('aws', '(\saws( |$|.|,))'),
	('kanban', '(\skanban( |$|.|,))'),
	('maven', '(\smaven( |$|.|,))'),
	('bamboo', '(\sbamboo( |$|.|,))'),
	('aspnet', '(\sasp\.net( |$|.|,))'),
	('dotnet', '(\sdot\s?net( |$|.|,))'),
	('ajax', '(\sajax( |$|.|,))'),
	('angular', '(\sangular( |$|.|,))'),
	('c#', '(\sc#( |$|.|,))'),
	JAVA,
	('cobol', '(\scobol( |$|.|,))'),
	('devops', '(\sdev\s?ops?( |$|.|,))'),
	('azure', '(\sazure( |$|.|,))'),
	('window', '(\swindows( |$|.|,))'),
	('jquery', '(\sjquery( |$|.|,))'),
]

criteria1_dict = {'SEARCH_LOCATION': "United States", "SEARCH_KEYWORD": "Software Engineer", "MAX_JOB_CYCLE": 2, "CRITERIA_KEYWORD":(PYTHON, JAVA)}
criteria2_dict = {'SEARCH_LOCATION': "Iowa, United States", "SEARCH_KEYWORD": "Software Developer", "MAX_JOB_CYCLE": 5}
CRITERIA_TUPLE = (criteria1_dict)

COUNTER_DICT = dict()

