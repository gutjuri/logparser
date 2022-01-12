input_dir = '../logs/' # The input directory of the log file

benchmark_settings = {
    'HDFS': {
        'log_file': 'HDFS/HDFS_2k.log', # The input log file name
        'log_format': '<Date> <Time> <Pid> <Level> <Component>: <Content>',
        'regex': [r'blk_-?\d+', r'(\d+\.){3}\d+(:\d+)?'], # Regular expression list for optional preprocessing (default: [])
        'minEventCount': 2, # AEL: The minimum number of events in a bin
        'merge_percent': 0.5, # AEL: The percentage of different tokens
        'st': 0.5, # Drain: Similarity threshold
        'depth': 4, # Drain: Depth of all leaf nodes
        'CT': 0.35, # IPLoM: The cluster goodness threshold (default: 0.35)
        'lowerBound': 0.25, # IPLoM: The lower bound distance (default: 0.25)
        'threshold': 0.9, # TODO Lenma: description (default: 0.9)
        'split_threshold': 3, # LKE: The threshold used to determine group splitting (default: 4)
        'rsupport': 10, # LogCluster: The minimum threshold of relative support, 10 denotes 10%
        'max_dist': 0.005,
        'k': 1, # LogMine: The message distance weight (default: 1)
        'levels': 2, # LogMine: The levels of hierarchy of patterns
        'groupNum': 15, # LogSig: The number of message groups to partition
        'maxChildNum': 4,
        'mergeThreshold': 0.1, # SHISO: Threshold for searching the most similar template in the children
        'formatLookupThreshold': 0.3, # SHISO: Lowerbound to find the most similar node to adjust
        'superFormatThreshold': 0.85, # SHISO: Threshold of average LCS length, determing whether or not to create a super format
        'support': 120, # SLCT: The minimum support threshold
        'tau': 0.7 # Spell: Message type threshold (default: 0.5)
    },

    'Hadoop': {
        'log_file': 'Hadoop/Hadoop_2k.log',
        'log_format': '<Date> <Time> <Level> \[<Process>\] <Component>: <Content>',
        'regex': [r'(\d+\.){3}\d+'],
        'minEventCount': 2,
        'merge_percent': 0.4,
        'st': 0.5,
        'depth': 4,
        'CT': 0.4,
        'lowerBound': 0.2,
        'threshold': 0.9,
        'split_threshold': 2,
        'rsupport': 10,
        'max_dist': 0.005,
        'k': 1,
        'levels': 2,
        'groupNum': 30,
        'maxChildNum': 4,
        'mergeThreshold': 0.002,
        'formatLookupThreshold': 0.3,
        'superFormatThreshold': 0.85,
        'support': 125,
        'tau': 0.7
    },

    'Spark': {
        'log_file': 'Spark/Spark_2k.log',
        'log_format': '<Date> <Time> <Level> <Component>: <Content>',
        'regex': [r'(\d+\.){3}\d+', r'\b[KGTM]?B\b', r'([\w-]+\.){2,}[\w-]+'],
        'minEventCount': 2,
        'merge_percent': 0.4,
        'st': 0.5,
        'depth': 4,
        'CT': 0.35,
        'lowerBound': 0.3,
        'threshold': 0.9,
        'split_threshold': 5,
        'rsupport': 10,
        'max_dist': 0.01,
        'k': 1,
        'levels': 2,
        'groupNum': 20,
        'maxChildNum': 4,
        'mergeThreshold': 0.002,
        'formatLookupThreshold': 0.3,
        'superFormatThreshold': 0.85,
        'support': 30,
        'tau': 0.55
    },

    'Zookeeper': {
        'log_file': 'Zookeeper/Zookeeper_2k.log',
        'log_format': '<Date> <Time> - <Level>  \[<Node>:<Component>@<Id>\] - <Content>',
        'regex': [r'(/|)(\d+\.){3}\d+(:\d+)?'],
        'minEventCount': 2,
        'merge_percent': 0.4,
        'st': 0.5,
        'depth': 4,
        'CT': 0.4,
        'lowerBound': 0.7,
        'threshold': 0.9,
        'split_threshold': 20,
        'rsupport': 0.5,
        'max_dist': 0.001,
        'k': 1,
        'levels': 2,
        'groupNum': 46,
        'maxChildNum': 4,
        'mergeThreshold': 0.003,
        'formatLookupThreshold': 0.3,
        'superFormatThreshold': 0.85,
        'support': 10,
        'tau': 0.7
    },

    'BGL': {
        'log_file': 'BGL/BGL_2k.log',
        'log_format': '<Label> <Timestamp> <Date> <Node> <Time> <NodeRepeat> <Type> <Component> <Level> <Content>',
        'regex': [r'core\.\d+'],
        'minEventCount': 2,
        'merge_percent': 0.5,
        'st': 0.5,
        'depth': 4,
        'CT': 0.4,
        'lowerBound': 0.01,
        'threshold': 0.7,
        'split_threshold': 30,
        'rsupport': 2,
        'max_dist': 0.01,
        'k': 2,
        'levels': 2,
        'groupNum': 500,
        'maxChildNum': 4,
        'mergeThreshold': 0.005,
        'formatLookupThreshold': 0.3,
        'superFormatThreshold': 0.85,
        'support': 6,
        'tau': 0.75
    },

    'HPC': {
        'log_file': 'HPC/HPC_2k.log',
        'log_format': '<LogId> <Node> <Component> <State> <Time> <Flag> <Content>',
        'regex': [r'=\d+'],
        'minEventCount': 5,
        'merge_percent': 0.4,
        'st': 0.5,
        'depth': 4,
        'CT': 0.58,
        'lowerBound': 0.25,
        'threshold': 0.8,
        'split_threshold': 10,
        'rsupport': 0.1,
        'max_dist': 0.0001,
        'k': 0.8,
        'levels': 2,
        'groupNum': 800,
        'maxChildNum': 3,
        'mergeThreshold': 0.003,
        'formatLookupThreshold': 0.6,
        'superFormatThreshold': 0.4,
        'support': 7,
        'tau': 0.65
    },

    'Thunderbird': {
        'log_file': 'Thunderbird/Thunderbird_2k.log',
        'log_format': '<Label> <Timestamp> <Date> <User> <Month> <Day> <Time> <Location> <Component>(\[<PID>\])?: <Content>',
        'regex': [r'(\d+\.){3}\d+'],
        'minEventCount': 2,
        'merge_percent': 0.4,
        'st': 0.5,
        'depth': 4,
        'CT': 0.3,
        'lowerBound': 0.2,
        'threshold': 0.6,
        'split_threshold': 2,
        'rsupport': 2,
        'max_dist': 0.005,
        'k': 1,
        'levels': 2,
        'groupNum': 25,
        'maxChildNum': 4,
        'mergeThreshold': 0.0002,
        'formatLookupThreshold': 0.3,
        'superFormatThreshold': 0.85,
        'support': 10,
        'tau': 0.5
    },

    'Windows': {
        'log_file': 'Windows/Windows_2k.log',
        'log_format': '<Date> <Time>, <Level>                  <Component>    <Content>',
        'regex': [r'0x.*?\s'],
        'minEventCount': 2,
        'merge_percent': 0.4,
        'st': 0.7,
        'depth': 5,
        'CT': 0.3,
        'lowerBound': 0.25,
        'threshold': 0.78,
        'split_threshold': 4,
        'rsupport': 0.2,
        'max_dist': 0.003,
        'k': 1,
        'levels': 2,
        'groupNum': 42,
        'mergeThreshold': 0.002,
        'maxChildNum': 3,
        'formatLookupThreshold': 0.3,
        'superFormatThreshold': 0.85,
        'support': 3,
        'tau': 0.7
    },

    'Linux': {
        'log_file': 'Linux/Linux_2k.log',
        'log_format': '<Month> <Date> <Time> <Level> <Component>(\[<PID>\])?: <Content>',
        'regex': [r'(\d+\.){3}\d+', r'\d{2}:\d{2}:\d{2}'],
        'minEventCount': 2,
        'merge_percent': 0.6,
        'st': 0.39,
        'depth': 6,
        'CT': 0.3,
        'lowerBound': 0.3,
        'threshold': 0.88,
        'split_threshold': 10,
        'rsupport': 40,
        'max_dist': 0.006,
        'k': 1,
        'levels': 2,
        'groupNum': 25,
        'maxChildNum': 3,
        'mergeThreshold': 0.005,
        'formatLookupThreshold': 0.3,
        'superFormatThreshold': 0.4,
        'support': 100,
        'tau': 0.55
    },

    'Andriod': {
        'log_file': 'Andriod/Andriod_2k.log',
        'log_format': '<Date> <Time>  <Pid>  <Tid> <Level> <Component>: <Content>',
        'regex': [r'(/[\w-]+)+', r'([\w-]+\.){2,}[\w-]+', r'\b(\-?\+?\d+)\b|\b0[Xx][a-fA-F\d]+\b|\b[a-fA-F\d]{4,}\b'],
        'minEventCount': 2,
        'merge_percent': 0.6,
        'st': 0.2,
        'depth': 6,
        'CT': 0.25,
        'lowerBound': 0.3,
        'threshold': 0.86,
        'split_threshold': 260,
        'rsupport': 1,
        'max_dist': 0.01,
        'k': 1,
        'levels': 2,
        'groupNum': 900,
        'maxChildNum': 4,
        'mergeThreshold': 0.002,
        'formatLookupThreshold': 0.3,
        'superFormatThreshold': 0.85,
        'support': 1,
        'tau': 0.95
    },

    'HealthApp': {
        'log_file': 'HealthApp/HealthApp_2k.log',
        'log_format': '<Time>\|<Component>\|<Pid>\|<Content>',
        'regex': [],
        'minEventCount': 2,
        'merge_percent': 0.6,
        'st': 0.2,
        'depth': 4,
        'CT': 0.25,
        'lowerBound': 0.3,
        'threshold': 0.5,
        'split_threshold': 50,
        'rsupport': 7,
        'max_dist': 0.008,
        'k': 1,
        'levels': 2,
        'groupNum': 200,
        'maxChildNum': 4,
        'mergeThreshold': 0.0001,
        'formatLookupThreshold': 0.3,
        'superFormatThreshold': 0.85,
        'support': 100,
        'tau': 0.5
    },

    'Apache': {
        'log_file': 'Apache/Apache_2k.log',
        'log_format': '\[<Time>\] \[<Level>\] <Content>',
        'regex': [r'(\d+\.){3}\d+'],
        'minEventCount': 2,
        'merge_percent': 0.4,
        'st': 0.5,
        'depth': 4,
        'CT': 0.3,
        'lowerBound': 0.4,
        'threshold': 0.91,
        'split_threshold': 5,
        'rsupport': 30,
        'max_dist': 0.005,
        'k': 1,
        'levels': 2,
        'groupNum': 8,
        'maxChildNum': 4,
        'mergeThreshold': 0.002,
        'formatLookupThreshold': 0.3,
        'superFormatThreshold': 0.85,
        'support': 5,
        'tau': 0.6
    },

    'Proxifier': {
        'log_file': 'Proxifier/Proxifier_2k.log',
        'log_format': '\[<Time>\] <Program> - <Content>',
        'regex': [r'<\d+\s?sec', r'([\w-]+\.)+[\w-]+(:\d+)?', r'\d{2}:\d{2}(:\d{2})*', r'[KGTM]B'],
        'minEventCount': 2,
        'merge_percent': 0.4,
        'st': 0.6,
        'depth': 3,
        'CT': 0.9,
        'lowerBound': 0.25,
        'threshold': 1,
        'split_threshold': 3,
        'rsupport': 10,
        'max_dist': 0.002,
        'k': 1,
        'levels': 2,
        'groupNum': 10,
        'maxChildNum': 4,
        'mergeThreshold': 0.002,
        'formatLookupThreshold': 0.3,
        'superFormatThreshold': 0.85,
        'support': 8,
        'tau': 0.85
    },

    'OpenSSH': {
        'log_file': 'OpenSSH/OpenSSH_2k.log',
        'log_format': '<Date> <Day> <Time> <Component> sshd\[<Pid>\]: <Content>',
        'regex': [r'(\d+\.){3}\d+', r'([\w-]+\.){2,}[\w-]+'],
        'minEventCount': 10,
        'merge_percent': 0.7,
        'st': 0.6,
        'depth': 5,
        'CT': 0.78,
        'lowerBound': 0.25,
        'threshold': 0.9,
        'split_threshold': 100,
        'rsupport': 0.1,
        'max_dist': 0.001,
        'k': 1,
        'levels': 2,
        'groupNum': 40,
        'maxChildNum': 4,
        'mergeThreshold': 0.002,
        'formatLookupThreshold': 0.3,
        'superFormatThreshold': 0.85,
        'support': 45,
        'tau': 0.8
    },

    'OpenStack': {
        'log_file': 'OpenStack/OpenStack_2k.log',
        'log_format': '<Logrecord> <Date> <Time> <Pid> <Level> <Component> \[<ADDR>\] <Content>',
        'regex': [r'((\d+\.){3}\d+,?)+', r'/.+?\s', r'\d+'],
        'minEventCount': 6,
        'merge_percent': 0.5,
        'st': 0.5,
        'depth': 5,
        'CT': 0.9,
        'lowerBound': 0.25,
        'threshold': 1,
        'split_threshold': 8,
        'rsupport': 3,
        'max_dist': 0.001,
        'k': 0.1,
        'levels': 2,
        'groupNum': 50,
        'maxChildNum': 4,
        'mergeThreshold': 0.002,
        'formatLookupThreshold': 0.3,
        'superFormatThreshold': 0.85,
        'support': 18,
        'tau': 0.9
    },

    'Mac': {
        'log_file': 'Mac/Mac_2k.log',
        'log_format': '<Month>  <Date> <Time> <User> <Component>\[<PID>\]( \(<Address>\))?: <Content>',
        'regex': [r'([\w-]+\.){2,}[\w-]+'],
        'minEventCount': 2,
        'merge_percent': 0.6,
        'st': 0.7,
        'depth': 6,
        'CT': 0.3,
        'lowerBound': 0.25,
        'threshold': 0.86,
        'split_threshold': 600,
        'rsupport': 0.2,
        'max_dist': 0.004,
        'k': 1,
        'levels': 2,
        'groupNum': 250,
        'maxChildNum': 4,
        'mergeThreshold': 0.002,
        'formatLookupThreshold': 0.3,
        'superFormatThreshold': 0.85,
        'support': 3,
        'tau': 0.6
    }
}
