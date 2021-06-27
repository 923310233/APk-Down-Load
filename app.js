'use strict';

const puppeteer = require('puppeteer');
const fs = require('fs');
var os = require("os");
var path = require("path");

var apkName = "";
//console.log(process.argv.length)
if (process.argv.length >= 3) {
    apkName = process.argv[2];
}
var globaltimeout = 120000;
(
    async () => {
        const browser = await puppeteer.launch({ headless: false})
        const page = await browser.newPage()
        var printerrname = './screenshot/'+apkName+".png"
        var url = 'https://play.google.com/store/apps/details?id='+apkName;
        
        console.log("requestUrl:" + url);
        await page.goto(url)
            .catch((err) => {
            });

        await page.waitFor(1500);

        // await page.click('#cc-accept-btn')
        //     .catch((err) => {
        //     });

        const category = await page.$eval('span.T32cc:nth-child(2) > a:nth-child(1)', el => el.innerText)
            .catch((err) => {
                console.log("error")
                page.screenshot({path: printerrname})
            });
        await page.screenshot({path: printerrname})
        console.log(category)
        // 不覆盖，追加方式

        let resultstring = apkName+","+category+os.EOL;
        fs.appendFile("category.csv",resultstring,(err) => {
            if (err) {

            } else {

            }
        });

        await browser.close();
    }
)()