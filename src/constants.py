

# Config key for message factories. 
MESSAGE_FACTORY_KEY         = "factory.messages"
# Config key for command factories. 
COMMAND_FACTORY_KEY         = "factory.commands"
# Config key for entity factories. 
ENTITY_FACTORY_KEY          = "factory.entities"
# Config key for property factories. 
PROPERTY_FACTORY_KEY        = "factory.properties"
#Config key for looking up jars for inspection by a LoadableTypeProcessor.
JAR_DIR_KEY                 = "loadabletypes.inspect.dir"
#Config key for specifying whether to do a deep inspection of jars for loadable types.
DEEP_JAR_INSPECTION_KEY     = "loadabletypes.inspect.deep"
# Default location for looking up jar files. 
DEFAULT_JAR_DIR             = "../jars"
# Default deep inspection. 
DEFAULT_DEEP_JAR_INSPECTION = True
#Config key for specifying jar names to ignore when finding loadable types.
IGNORE_JARS_KEY             = "loadabletypes.ignore"
# Default list of jar names to ignore when finding loadable types. 
DEFAULT_IGNORE_JARS         = "rescuecore2.jar"

# Config key for the kernel host name. 
KERNEL_HOST_NAME_KEY        = "kernel.host"
# Default kernel host name. 
DEFAULT_KERNEL_HOST_NAME    = "localhost"
# Config key for the kernel port number. 
KERNEL_PORT_NUMBER_KEY      = "kernel.port"
# Default kernel port number. 
DEFAULT_KERNEL_PORT_NUMBER  = 7000
# Config key for the gis port number. 
GIS_PORT_NUMBER_KEY         = "gis.port"
# Default gis port number. 
DEFAULT_GIS_PORT_NUMBER     = 7001

# The random seed key. 
RANDOM_SEED_KEY             = "random.seed"
# The random implementation class key. 
RANDOM_CLASS_KEY            = "random.class"
# The default random implementation class. 
RANDOM_CLASS_DEFAULT        = "org.uncommons.maths.random.MersenneTwisterRNG"

# The name of the communication model class. 
COMMUNICATION_MODEL_KEY     = "kernel.communication-model"
# The name of the perception class. 
PERCEPTION_KEY              = "kernel.perception"

# Config key for the top-level score function. 
SCORE_FUNCTION_KEY          = "score.function"

# Prefix for entity URNs. 
ENTITY_URN_PREFIX           = "entity:"
# Prefix for property URNs. 
PROPERTY_URN_PREFIX         = "property:"
# Prefix for command URNs. 
COMMAND_URN_PREFIX          = "command:"
# Prefix for message URNs. 
MESSAGE_URN_PREFIX          = "message:"
