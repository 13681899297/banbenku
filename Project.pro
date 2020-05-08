{
    "GlobalVar": [
    ],
    "MainSeq": {
        "seq": "Main"
    },
    "OpenFlow": "[\n    {\n        \"seq\": \"Main\"\n    },\n    {\n        \"seq\": \"LoginCSM\"\n    },\n    {\n        \"seq\": \"ProductsPage\"\n    },\n    {\n        \"seq\": \"GetData\"\n    }\n]\n",
    "ProInfo": {
        "ProChange": "2020/05/08 15:18:27",
        "ProCreate": "2020/05/08 14:28:04",
        "ProDesc": "",
        "ProImports": "",
        "ProIsAdminRun": "1",
        "ProName": "YeHongJun_KaoShi",
        "ProStudio": "2020.2.0.20",
        "ProTag": "",
        "ProUserID": "fb990eba74c441e3b7bd2a3fa20d550c",
        "ProVersion": "1.0.0.0"
    },
    "SequenceGroup": [
    ],
    "SequenceList": [
        {
            "group": "",
            "num": "1",
            "sdc": "",
            "seq": "Main",
            "sop": "Close",
            "spy": "Main"
        },
        {
            "group": "",
            "num": "1",
            "sdc": "",
            "seq": "LoginCSM",
            "sop": "Close",
            "spv": [
                {
                    "inpar_Order": "",
                    "inpar_filetype": "",
                    "inpar_helpdesc": "",
                    "inpar_init": "",
                    "inpar_required": "0",
                    "inputpar": "",
                    "vardef": "'TVlUqIwIyp0eXB=='",
                    "vardesc": "",
                    "varname": "password",
                    "varpasstype": "1",
                    "varrobot": "",
                    "vartype": "2"
                },
                {
                    "inpar_Order": "",
                    "inpar_filetype": "",
                    "inpar_helpdesc": "",
                    "inpar_init": "",
                    "inpar_required": "0",
                    "inputpar": "",
                    "vardef": "'ceshi001'",
                    "vardesc": "",
                    "varname": "userName",
                    "varpasstype": "1",
                    "varrobot": "",
                    "vartype": "1"
                },
                {
                    "inpar_Order": "",
                    "inpar_filetype": "",
                    "inpar_helpdesc": "",
                    "inpar_init": "",
                    "inpar_required": "0",
                    "inputpar": "",
                    "vardef": "'http://122.112.200.222:9080/login.action'",
                    "vardesc": "",
                    "varname": "url",
                    "varpasstype": "1",
                    "varrobot": "",
                    "vartype": "1"
                }
            ],
            "spy": "Main"
        },
        {
            "group": "",
            "num": "1",
            "sdc": "",
            "seq": "ProductsPage",
            "sop": "Close",
            "spy": "Main"
        },
        {
            "group": "",
            "num": "1",
            "sdc": "",
            "seq": "GetData",
            "sop": "Close",
            "spr": [
                {
                    "vardef": "7",
                    "vardesc": "",
                    "varname": "pv_maxPageNumber"
                },
                {
                    "vardef": "'i-Search-05'",
                    "vardesc": "",
                    "varname": "pv_key"
                }
            ],
            "spv": [
                {
                    "inpar_Order": "",
                    "inpar_filetype": "",
                    "inpar_helpdesc": "",
                    "inpar_init": "",
                    "inpar_required": "0",
                    "inputpar": "",
                    "vardef": "",
                    "vardesc": "",
                    "varname": "lv_totalResult",
                    "varpasstype": "1",
                    "varrobot": "",
                    "vartype": "1"
                },
                {
                    "vardef": "",
                    "vardesc": "",
                    "varname": "lv_pageResult",
                    "varpasstype": "1",
                    "vartype": "1"
                }
            ],
            "spy": "Main"
        }
    ]
}
