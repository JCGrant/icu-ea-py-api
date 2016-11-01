# ICU eActivities API

A Python API for Imperial College Union's [eActivities](https://eactivities.union.ic.ac.uk).

## Install
    pip install icu-ea-api

## Example

    from icu_ea_api import ICUEActivitiesAPI

    csp_code = 000
    api_key = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'

    society_api = ICUEActivitiesAPI(csp_code, api_key)

    print(society_api.list_members(year='16-17'))
