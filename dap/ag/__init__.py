# Copyright 2018 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Autograd modules.

These are mostly experimental implementations of differentiable potentials using
autograd (https://github.com/HIPS/autograd).

Autograd is essentially limited to functions. It does not support gradients on
classes. Autograd is built on top of numpy though, which makes it an all Python
approach to differentiable programming that is pretty easy to use.

"""
