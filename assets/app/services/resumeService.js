app.service('resumeService', function ($http, $q) {
    "use strict";
    return {
        createResume: function (data) {
            var defer = $q.defer();
            $http({
                method: 'POST',
                url: '/api/resumes/',
                data: JSON.stringify(data)
            }).success(function (data, status, headers, config) {
                defer.resolve(data);
            }).error(function (data, status, headers, config) {
                defer.reject(status);
            });
            return defer.promise;
        },
        listResumes: function () {
            var defer = $q.defer();
            $http({
                method: 'GET',
                url: '/api/resumes/'
            }).success(function (data, status, headers, config) {
                defer.resolve(data);
            }).error(function (data, status, headers, config) {
                defer.reject(status);
            });
            return defer.promise;
        },
        updateResume: function (data) {
            var defer = $q.defer();
            $http({
                method: 'PUT',
                url: '/api/resumes/' + data.id + '/',
                data: data
            }).success(function (data, status, headers, config) {
                defer.resolve(data);
            }).error(function (data, status, headers, config) {
                defer.reject(status);
            });
            return defer.promise;
        },
        deleteResume: function (data) {
            var defer = $q.defer();
            $http({
                method: 'DELETE',
                url: '/api/resumes/' + data.id + '/'
            }).success(function (data, status, headers, config) {
                defer.resolve(data);
            }).error(function (data, status, headers, config) {
                defer.reject(status);
            });
            return defer.promise;
        }
    };
});
