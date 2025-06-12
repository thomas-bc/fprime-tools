#####
# '{{cookiecutter.deployment_name}}' Deployment:
#
# This registers the '{{cookiecutter.deployment_name}}' deployment to the build system. 
# Custom components that have not been added at the project-level should be added to 
# the list below.
#
#####

###
# Topology and Components
###
# Add components defined within the deployment directory here, if any
# add_fprime_subdirectory("${CMAKE_CURRENT_LIST_DIR}/MyComponent/")

add_fprime_subdirectory("${CMAKE_CURRENT_LIST_DIR}/Top/")

register_fprime_deployment(
    SOURCES
        "${CMAKE_CURRENT_LIST_DIR}/Main.cpp"
    DEPENDS
        ${FPRIME_CURRENT_MODULE}_Top
)
