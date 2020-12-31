const path = require("path");
const OptimizeCssAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const TerserPlugin = require("terser-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
  entry: {
    bootstrapStyling: "./src/js/bootstrapStyling.js",
    outlookStyling: "./src/js/outlookStyling.js",
  },
  output: {
    publicPath: "",
    path: path.resolve(__dirname, "prod"),
    filename: "jsFiles/[name].js",
  },
  optimization: {
    minimizer: [new OptimizeCssAssetsPlugin(), new TerserPlugin()],
  },
  module: {
    rules: [
      {
        //HTML loader Exports HTML as string, hence it can capture file extention names
        test: /\.html$/,
        use: ["html-loader"],
      },

      {
        test: /\.(png|svg|jpe?g|gif)$/i,
        use: [
          {
            loader: "file-loader",
            options: {
              // name: "[name].[hash].[ext]",
              name: "[name].[ext]",
              outputPath: "imgsFolder/",
            },
          },
        ],
      },

      {
        // Apply rule for fonts files
        test: /\.(woff|woff2|ttf|otf|eot)$/,
        use: [
          {
            // Using file-loader
            loader: "file-loader",
            options: {
              name: "[name].[hash].[ext]",
              outputPath: "fontsFolder/",
            },
          },
        ],
      },

      {
        test: /\.css$/i,
        use: [
          MiniCssExtractPlugin.loader, //Extracts css into files
          "css-loader", //Tuns css into common js
        ],
      },

      {
        //transpiles SCSS to js
        test: /\.s[ac]ss$/i,
        use: [
          MiniCssExtractPlugin.loader, //Extract css into files
          "css-loader", //Turns css into common js
          "sass-loader", //Turns scss into css
        ],
      },
    ],
  },

  plugins: [
    new CleanWebpackPlugin(),
    new CleanWebpackPlugin({ cleanStaleWebpackAssets: false }),
    new MiniCssExtractPlugin({ filename: "[name].css" }),
    new HtmlWebpackPlugin({
      template: "./src/template.html",
      minify: {
        collapseWhitespace: true,
        removeComments: true, // false for Vue SSR to find app placeholder
        removeEmptyAttributes: true,
      },
    }),
  ],
};
